def generate_hashtag(s):
    return '#'+' '.join([str(x).capitalize() 
                        for x in str(s).split()]).replace(
                        ' ', '') if len(s.replace(' ', '')) < 140 or len(
                        s.replace(' ', '')) == 0 else False

# " Hello there thanks for trying my Kata"  -->  "#HelloThereThanksForTryingMyKata"
# "    Hello     World   "                  -->  "#HelloWorld"
# ""                                        -->  false
s = " Hello there thanks for trying my Kata"
s_2 = ''
s_3 = 'UkRYeHQaRNB qCoylpPliUT QVjaBPi CS  aHnMHeuuFZK AgChcoKgS h nrjGiWKPIlk gaGRDIDcHcG BDEmTsVouNb bz ElWUnkdP CqTqPuNthnW b F Z Aehn  p jhzLIlyQg'
print(generate_hashtag(s))
print(generate_hashtag(s_3))
print(len(s_3))

