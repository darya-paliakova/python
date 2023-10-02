import re

initialString = """homEwork:
 tHis iz your homeWork, copy these Text to variable.



 You NEED TO normalize it fROM letter CASEs point oF View. also, create one MORE senTENCE witH LAST WoRDS of each existING SENtence and add it to the END OF this Paragraph.



 it iZ misspeLLing here. fix“iZ” with correct “is”, but ONLY when it Iz a mistAKE.



 last iz TO calculate nuMber OF Whitespace characteRS in this Tex. caREFULL, not only Spaces, but ALL whitespaces. I got 87."""

correctSpellString = (initialString.replace(' iz ', ' is ')
                      .replace('Tex.', 'text.')
                      .replace("fix", "fix "))

splitString = re.split('([\n.!?:] *)', correctSpellString)

filteredList = []
for eachItem in splitString:
    if (eachItem != "\n "
            and eachItem != "\n"
            and eachItem != ""
            and eachItem != "."
            and eachItem != ". "
            and eachItem != ","
            and eachItem != ":"):
            filteredList.append(eachItem)

newString = ''
for eachItem in filteredList:
    splitItem = re.split(' ', eachItem)
    newString += ''.join(splitItem[-1])
    if (filteredList.index(eachItem)+1) != len(filteredList):
        newString += ' '
    if (filteredList.index(eachItem) + 1) == len(filteredList):
        newString += '.'

triggerWord = 'Paragraph.'
fullString = correctSpellString.replace(triggerWord, triggerWord + ' ' + newString)

splitString = re.split('([\n.!?:] *)', fullString)
normalizedString = ''.join([i.capitalize() for i in splitString])

sumWhiteSpaces = 0
# for i in normalizedString:
#     if i.isspace():

for i in re.findall("\s", normalizedString):
    sumWhiteSpaces += 1

updatedSting = normalizedString.replace('87', str(sumWhiteSpaces))
print(updatedSting)



