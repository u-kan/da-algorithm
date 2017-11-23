# coding: utf-8
import copy

Students = {
 '1':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '2':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '3':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '4':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '5':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '6':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '7':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '8':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '9':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '10':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '11':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '12':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '13':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '14':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '15':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '16':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '17':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '18':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '19':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '20':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '21':  ['a', 'b', 'c', 'd', 'e', 'f', 'g'],
 '22':  ['a', 'b', 'c', 'd', 'e', 'f', 'g']}

Schools = {
 'a':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'b':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'c':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'd':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'e':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'f':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'g':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']}


proposers_capacities = {
    'a': 2,
    'b': 1,
    'c': 3,
    'd': 4,
    'e': 1,
    'f': 1,
    'g': 3
}
"""
Schools = {
 'a':  {
     ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 }
 'b':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'c':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'd':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'e':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'f':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36'],
 'g':  ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36']}
"""

# '  '  の中が　Students / Schools
apply = 'Schools'

if (apply == 'Students'):
    proposerprefers = Students
    proposeeprefers = Schools 
elif (apply == 'Schools'):
    proposerprefers = Schools
    proposeeprefers = Students
else:
    print 'type Students or Schools in apply'

proposers = sorted(proposerprefers.keys()) # 学校
proposees = sorted(proposeeprefers.keys()) # 学生
 
def check(engaged):
    inverseengaged = dict((v,k) for k,v in engaged.items())
    for she, he in engaged.items():
        shelikes = proposeeprefers[she]
        shelikesbetter = shelikes[:shelikes.index(he)]
        helikes = proposerprefers[he]
        helikesbetter = helikes[:helikes.index(she)]
        for proposer in shelikesbetter:
            proposersgirl = inverseengaged[proposer]
            proposerlikes = proposerprefers[proposer]
            if proposerlikes.index(proposersgirl) > proposerlikes.index(she):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (she, proposer, he, proposersgirl))
                return False
        for proposee in helikesbetter:
            girlsproposer = engaged[proposee]
            proposeelikes = proposeeprefers[proposee]
            if proposeelikes.index(girlsproposer) > proposeelikes.index(he):
                print("%s and %s like each other better than "
                      "their present partners: %s and %s, respectively"
                      % (he, proposee, she, girlsproposer))
                return False
    return True
 
def matchmaker():
    proposersfree = proposers[:]
    engaged  = {}
    proposerprefers2 = copy.deepcopy(proposerprefers)
    proposeeprefers2 = copy.deepcopy(proposeeprefers)
    while proposersfree:
        proposer = proposersfree.pop(0)
        proposerslist = proposerprefers2[proposer]
        proposee = proposerslist.pop(0)
        fiance = engaged.get(proposee)
        if not fiance:
            # She's free
            engaged[proposee] = proposer
            print("  %s and %s" % (proposer, proposee))
        else:
            # The bounder proposes to an engaged lass!
            proposeeslist = proposeeprefers2[proposee]
            if proposeeslist.index(fiance) > proposeeslist.index(proposer):
                # She prefers new proposer
                engaged[proposee] = proposer
                print("  %s dumped %s for %s" % (proposee, fiance, proposer))
                if proposerprefers2[fiance]:
                    # Ex has more girls to try
                    proposersfree.append(fiance)
            else:
                # She is faithful to old fiance
                if proposerslist:
                    # Look again
                    proposersfree.append(proposer)
    return engaged
 
 
def matchmaker_ver2():
    proposeesfree = proposees[:]
    engaged  = {}
    proposerprefers2 = copy.deepcopy(proposerprefers)
    proposeeprefers2 = copy.deepcopy(proposeeprefers)
    while proposeesfree:
        proposee = proposeesfree.pop(0)
        proposeeslist = proposeeprefers2[proposee]
        proposer = proposeeslist.pop(0)
        fiance = engaged.get(proposee)
        capacity = proposers_capacities[proposer]
        proposer_selected_count = engaged.values().count(proposer)
        if proposer_selected_count < capacity:
            engaged[proposee] = proposer
            print("  %s and %s" % (proposer, proposee))
        else:
            # The bounder proposes to an engaged lass!
            proposerslist = proposerprefers2[proposer]
            candidate_proposees = [k for k,v in engaged.items() if v == proposer]
            for candidate in candidate_proposees:
                if proposerslist.index(candidate) > proposerslist.index(proposee):
                    # She prefers new proposer
                    del engaged[candidate]
                    engaged[proposee] = proposer
                    print("  %s dumped %s for proposer %s has now %s" % (proposee, fiance, proposer, engaged))
                    if proposeeprefers2[candidate]:
                        # Ex has more girls to try
                        proposeesfree.append(candidate)
                else:
                    # She is faithful to old fiance
                    if proposeeslist: # proposee の好きなproposer のリスト
                        # Look again
                        proposeesfree.append(proposee)
                break
    ret = {}
    for k, v in engaged.items():
        if ret.get(v):
            ret[v].append(k)
        else:
            ret[v] = [k]
    return ret 
 
print('\nEngagements:')
engaged = matchmaker()
 
print('\nMultiple Engagements is Available:')
multi_engaged = matchmaker_ver2()
print(multi_engaged)

print('\nCouples:')
print('  ' + ',\n  '.join('%s is engaged to %s' % couple
                          for couple in sorted(engaged.items())))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')
 
print('\n\nSwapping two fiances to introduce an error')
engaged[proposees[0]], engaged[proposees[1]] = engaged[proposees[1]], engaged[proposees[0]]
for proposee in proposees[:2]:
    print('  %s is now engaged to %s' % (proposee, engaged[proposee]))
print()
print('Engagement stability check PASSED'
      if check(engaged) else 'Engagement stability check FAILED')
