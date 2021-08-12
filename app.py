import streamlit as st
import spacy_streamlit
from spacy.language import Language

models = ["en_ushmm_rules"]

default_text = '''
I would bring it home at night so we had it.
And my grandfather was getting weaker and weaker.
He couldn't eat.
This was really awful, so we kept on saving his bread.
And his wish was to live so long that we can pick up his rations.
This was his inheritance because he said he lost all his gold, he can't leave us anything else.
What we did he died the day before the rations came, and we didn't report it until the following day, we picked it up and then I reported the death, so we had this extra little food and an extra loaf of bread, which later I left if in Auschwitz because we're still hoarding and we're still afraid to let go and eat everything a once.
But the existence in Lodz Ghetto was awful.
They also had the criminal police, _______, this was German police.
They had their headquarters in a little church, and they would call people in and say what do you have?
Our landlord, he was the head of fences before the war.
A real, very unsavory character, but he had a heart of gold.
And he must have had money.
They beat him to death.
They let him out, he died a day later.
But he was like -- his face was like liver.
He never told them what he had.
They called my mother in.
They said we heard you are a rich dentist from __________.
What do you have?
And she said, "Well, I have a couple of gold chains, I have a little diamond."
And they said, bring it in.
So, she 14 brought it in and they let her go.
So, they were satisfied.
If she would have said she had nothing, they would have tortured her.
This between the ___________ and the Jews under commando, this was pretty tight situation over there.
And then they started evacuations.
They were evacuating constantly people.
One of the worst actions was when they took the children out.
Orders came that they have to take the children, they're going to take them to better places.
There will be fresh air and farms and the people put signs on it and they mobilized all the Jewish police including all the people who worked for the health department, including my mother, and they had to go and collect the children.
The children were being taken voluntarily by the parents, taken down, because they couldn't hide them.
The moment the family would hide a child, the rations would be taken away, so not only the child didn't have the rations, but the family wouldn't have the rations.
Our next door neighbors had hidden a child and they struggled.
Unfortunately she died later, but it was -- and then they were taking the old people.
They would make you line up on the street and get out and just select the old people and the children Now, one of the worst actions was around the Jewish holidays, this was '44, I believe.
And we lived on the corner, and the lady the one who was our so-called landlady, she was the wife of the guy who was killed.
Before the war she was in Argentina.
So, we started lining up on one street and she called everybody up and she said forget it.
This is not our street.
Our address is the next street.
There were two entrances there.
She said, all of you go back home and hide.
Just sit quiet, don't open the window, don't stand next to windows.
At that time she had hidden some children and my grandparents.
We didn't know where they were, somewhere.
They had all kinds of nooks and crannies in that building, and we had all hidden quietly, and at noon they rang the whistles and they stopped the action.
So, they were ready to call that second street, where we were, they called it off, so we were saved.
If she would have -- we walked out and somebody said to us, someone who knew us and said, where are your parents, and my mother said, hidden.
He said, that's silly, they'll find them.
They'll kill them.
'''
visualizers = ['ner']
spacy_streamlit.visualize(models, default_text, visualizers=visualizers)
