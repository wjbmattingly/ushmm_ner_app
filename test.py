import spacy
text = '''

DAVID KOCHALSKI July 28, 1994 Q: I need you to start off by telling me your name, place of birth, and date of birth?
A: My name David Kochalski.
I was born in a small town called _____________, and I was born May 5, 1928.
Q: Tell me a little bit about your family life before the war?
A: Well, we were very hard working, six children, father and mother and we had a small mill, flour, buckwheat.
We were not prosperous but comfortable.
Q: Did you go to a public school, a private school?
A: I went to two schools.
One was a public school in the morning.
In the afternoon I went to a religious school until almost late at night.
Q: So your family was fairly religious?
A: Yes.
Q: And Judaism was important to you?
A: Well, I raised in the spirit of Judaism.
Q: Now, when you went to the public school you had a lot of friends who were not Jewish?
A: No, the school itself, in this little city, was segregated between Catholics and Jews.
Mind you, it was a small town, and I would say the majority of the people in that small town were Jewish people.
Inside the town, somehow, I don't know why, but they separated us Jewish children and Catholic children.
As you know, most of the people in Poland were Catholic.
Q: Did you have friends who were Catholics?
A: Yes, I used to have friends.
Q: Did you feel any anti-semitism growing up?
A: Yes, I did.
I felt it, maybe not personally, but I knew of a lot of incidents whereby either they were small little -- I would call it -- we were separated, in other words, but hardly got together, and there were incidents.
Incidents, not pleasant incidents, because we were 2 called in from the house, people regardless of how religious we were, did not believe that we were really religious people.
Q: Were there any incidents with your brothers or sisters that you remember?
A: No, other than we were a lovely family.
Q: Were there a lot of cultural or social organizations, political organizations in the town?
A: Yes there were Zionists in the city.
There were Socialists, there were Communists, even though at that time Communists had to go underground, and religious institutions.
Q: Were your parents active in the Zionist movement?
A: My parents were, I would say, Zionists, and very religious.
Q: What did you know about Hitler and the rise of Nazism before the war?
A: I was aware what was going on even though I was a very young youngster.
My father used to subscribe to many newspapers, Jewish in origin and non-Jewish papers, papers tha
'''
nlp = spacy.load("ushmm_sm_final")
doc = nlp(text)
for ent in doc.ents:
    print (ent.text, ent.label_)
