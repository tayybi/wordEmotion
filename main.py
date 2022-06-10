
import string

#getting all data from file
text =open("textdata.txt",encoding='utf-8').read()
lowerCase=text.lower()
print(lowerCase)

#cleaning data
cleanText=lowerCase.translate(str.maketrans('','',string.punctuation))
print(cleanText)

tokenizedWord=cleanText.split()
print(tokenizedWord)

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

finalWords=[]
for words in tokenizedWord:
    if words not in stop_words:
        finalWords.append(words)
print(finalWords)

with open('emotions.txt','r') as file:
    for line in file:
        clearLine=line.replace("\n","").replace(",","").replace("'","").strip()
        words , emotions=clearLine.split(':')
        print("word :"+  words + " " + "Emotions :" + emotions)
