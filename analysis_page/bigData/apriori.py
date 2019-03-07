import sys
from itertools import chain, combinations
from collections import defaultdict
from optparse import OptionParser
from . import models
import json
import itertools
import pprint


def subsets(arr):
	""" Returns non empty subsets of arr"""
	return chain(*[combinations(arr, i + 1) for i, a in enumerate(arr)])


def returnItemsWithMinSupport(itemSet, transactionList, minSupport, freqSet):
	"""calculates the support for items in the itemSet and returns a subset
	of the itemSet each of whose elements satisfies the minimum support"""
	_itemSet = set()
	localSet = defaultdict(int)

	for item in itemSet:
		for transaction in transactionList:
			if item.issubset(transaction):
				freqSet[item] += 1
				localSet[item] += 1

	for item, count in localSet.items():
		support = float(count)/len(transactionList)

		if support >= minSupport:
			_itemSet.add(item)

	return _itemSet


def joinSet(itemSet, length):
        """Join a set with itself and returns the n-element itemsets"""
        return set([i.union(j) for i in itemSet for j in itemSet if len(i.union(j)) == length])


def getItemSetTransactionList(data_iterator):
    transactionList = list()
    itemSet = set()
    for record in data_iterator:
        transaction = frozenset(record)
        transactionList.append(transaction)
        for item in transaction:
            itemSet.add(frozenset([item]))              # Generate 1-itemSets
    return itemSet, transactionList

def runApriori(data_iter, minSupport, minConfidence):
    Rcount = 0
    """
    run the apriori algorithm. data_iter is a record iterator
    Return both:
     - items (tuple, support)
     - rules ((pretuple, posttuple), confidence)
    """
    itemSet, transactionList = getItemSetTransactionList(data_iter)

    freqSet = defaultdict(int)
    largeSet = dict()
    # Global dictionary which stores (key=n-itemSets,value=support)
    # which satisfy minSupport

    assocRules = dict()
    # Dictionary which stores Association Rules

    oneCSet = returnItemsWithMinSupport(itemSet,
                                        transactionList,
                                        minSupport,
                                        freqSet)

    currentLSet = oneCSet
    k = 2
    while(currentLSet != set([])):
        largeSet[k-1] = currentLSet
        currentLSet = joinSet(currentLSet, k)
        currentCSet = returnItemsWithMinSupport(currentLSet,
                                                transactionList,
                                                minSupport,
                                                freqSet)
        currentLSet = currentCSet
        k = k + 1

    def getSupport(item):
            """local function which Returns the support of an item"""
            return float(freqSet[item])/len(transactionList)

    toRetItems = []
    for key, value in largeSet.items():
        toRetItems.extend([(tuple(item), getSupport(item))
                           for item in value])

    toRetRules = []
    for key, value in largeSet.items():
        for item in value:
            _subsets = map(frozenset, [x for x in subsets(item)])
            for element in _subsets:
                remain = item.difference(element)
                if len(remain) > 0:
                    confidence = getSupport(item)/getSupport(element)
                    if confidence >= minConfidence:
                        Rcount += 1
                        toRetRules.append(((tuple(element), tuple(remain)),
                                           confidence))

    return toRetItems, toRetRules, Rcount


def printResults(items, rules, rcount):
	ruleR = []
	ruleR2 = []
	ruleR3 = []

	Return_JsonValue = []
	JsonValue = {}
	JsonValue2 = {}
	ruleR3.append('{"n":"Route", "children":[')
	count = 0

	#for item, support in sorted(items, key=lambda support: support[1]):
		#print ("item: %s , %.3f" % (str(item), support))

	for rule, confidence in sorted(rules, key=lambda confidence: confidence[1]):
		pre, post = rule

		#print ("Rule: %s ==> %s , %.3f" % (str(pre), str(post), confidence))
		replace = str(pre).replace("('", '{"n":"')
		replace2 = replace.replace("', '", '", "children":[{"n":"')
		replace3 = replace2.replace("'", '"')
		replace4 = replace3.replace(",)", ",")
		replace5 = replace4.replace(")", ",")

		# flow2.csv 추가
		replace6 = replace5.replace('""""', '""')
		replace7 = replace6.replace('""', '"')

		replaceP = str(post).replace("('", '"children":[{"n":"')
		replaceP2 = replaceP.replace("', '", '", "children":[{"n":"')
		replaceP3 = replaceP2.replace("')", '"}]}]}')
		replaceP4 = replaceP3.replace("',)", '"}]}')

		# flow2.csv 추가
		replaceP5 = replaceP4.replace('""""', '""')
		replaceP6 = replaceP5.replace('""', '"')

		ruleR = replace7
		ruleR2 = replaceP6

		ruleR3.append(ruleR)
		ruleR3.append(ruleR2)

		#if len(str(pre)) > 10:
		#	ruleR3.append("]}")
		string = str(pre)
		string2 = "')"
		a = string.find(string2)

		if string2 in str(pre):
			ruleR3.append("]}")

		if count == rcount-1:
			count = count

		else:
			ruleR3.append(",")

		count = count+1

	ruleR3.append("]}")
	return ruleR3


def dataFromFile(fname):
	for line in fname:
		record = frozenset(line)
		yield record


def main(dataFlow):
	Rules = []
	inFile = dataFromFile(dataFlow)
	minSupport="0.04"
	minConfidence="0.3"
	items,rules,rcount=runApriori(inFile,float(minSupport),float(minConfidence))
	Rules = printResults(items,rules,rcount)
	Rules2 = json.dumps(Rules)
	return Rules
if __name__ == '__main__':
	main()
