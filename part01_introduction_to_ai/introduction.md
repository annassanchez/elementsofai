# Chapter 01: what is AI?
## I. How should we define AI?
<h3>In our very first section, we'll become familiar qith the concept of AI by looking intro it's definition and some examples.</h3>
As you have probably noticed, AI is currently a "hot topic": media coverage and public discussion about AI is almost impossible to avoid. However, you may also have noticed that AI means different things to different people. For some, AI is about artificial life-forms that can surpass human intelligence, and for others, almost any data processing technology can be called AI.
To set the scene, so to speak, we'll discuss what AI is, how it can be defined, and what other fields or technologies are closely related. Before we do so, however, we'll highlight three applications of AI that illustrate different aspects of AI. We'll return to each of them throughout the course to deepen our understanding.
![](images/1_1.svg)

### **Application 01. Self-driving cars**
Self-driving cars require a combination of AI techniques of many kinds: seach and planning to find the most convenient route from A to B, computer vision to identify obstacles, and decision making under uncertainty to cope with the complex and dynamic enviroment. Each of these must work with almost flawless precision in order to avoid accidents.
The same technologies are also used in other autonomous systems such as delivery robots, flying drones, and autonomous ships.
**Implications:** road safety should eventually improe as the reliability of the systems syroassses human level. The efficiency of logistics chains when moving goods should improve. Humans move into a supervisory role, keeping an eye on what's going on while machines take care of the driving. Since transportation is such cructial element in our daily life, it is likely that there are also some implications that we haven't even thought about yet.
![](images/1_2.svg)
### **Application 02. Content Recommendation**
A lot of the information that we encounter in the course of a typical day is personalized. Examples include Facebook, Twitter, Instagram, and other social media content; online advertisements; music recommendations on Spotify; movie recommendations on Netflix, HBO and other streaming services. Many online publishers such as newspapers' and broadcasting companies' websites as well as search engines such as Google also personalizethe content they offer.
While the frontpage of the printed version of the *New York Times* or *China Daily* is the same for all readers, the frontpage od the online verrsion is different for each user. The algorithms that determine the content that you see are based on AI.
**Implications**: while many companies don'0t want to reveal the details od their algorithms, being aware of the basic principles helps you understand the potential implications: these involve so called filter bubbles, echo-chambers, troll factores, fake news, and new forms of propaganda.
![](images/1_3.svg)
### **Application 03. Image and video processing**
Face recognition is already a commodity used in many customer, business, and government applications such as organizing your photos according to people, automatic tagging on social media, and passport control. Similar techniques can be used to recognize other cars and obstacles around an anotonomous car, or the estimate [wildlife populations](https://valohai.com/showcase/marais-elephant/), just a few examples.
AI can be used to generate or alter cisual content. Examples already in use today include style transfer, by ehich you can adapt your personal photos to look like they were painted by Vincent Van Gogh, and computer generated characters in motion pictures such as *Avatar*, *the Lord of the Rings*, and popular Pixar animations where the animated characters replicate gestures made by real human actors.
**Implications**: when such techniques advance and become more widely available, it will be easy to create natural looking fake videos of events that are impossible to distingish from real footage. This challenges the notion that 'seeing is believing'.
![](images/1_4.svg)
### That is, and what isn't AI? Not an easy question!
The popularity of AI in the media is in part due to the fact that people have started using the term when they refer to things that used to be called by other names. You can see almost the anything ffrom statistics and business analytics to manually encoded if-then rules called AI. Why is this so? Why is the public perception of AI so nebolous? Let's look at a few reasons:

|   	|   	|
|---	|---	|
| ![](images/1_5.svg)	| reason 01: no official agreed deffinition<br>Even AI researchers have no exact definition of AI. The field is rather being constantly redefined when some topics are classified as non-AI, and new topics emerge.<br>There's an old (geeky) joke that AI is defined as "cool things that computers can't do". The irony is taht under this definition, AI can never make any progress: as soon as we find a way to do somethind cool with a computer, it stops being an AI problem. How ever, there is an element of truth in this definition. Fifty years ago, for instance, automatic methods for search and planning were considered to belong to the domain of AI. Nowadays such methods are taught to every computer science student. Similarly, certain methods for processing uncertain information are becoming so well understood that they are likely to be moved from AI to statistics or probability very soon. 	|
| ![](images/1_6.svg) 	| reason02: the legacy of science fiction<br>The confusion about the meaning of AI is made worse by the visions of AI present in various literary and cinematic works of science fiction. Science fiction stories often feature friendly humanoid servants that provide overly-detailed factoids or witty dialogue, but can sometimes follow the steps of Pinocchio and start to wonder if they can become human. Another class of humanoid beings in sci-fi espouse sinister motives and turn against their masters in the vein of old tales of sorcerers’ apprentices, going back to the [Golem of Prague](https://en.wikipedia.org/wiki/Golem) and beyond.<br>Often the robothood of such creatures is only a thin veneer on top of a very humanlike agent, which is understandable as most fiction -- even since science fiction -- needs to be relatable by human readers who would otherwise be alienated by intelligence that is too different and strange. Most science fiction is thus best read as metaphor for the current human condition, and robtos could be seen as stand-ins for repressed sections of society, or perhaps our search for the meaning of life. 	|
| ![](images/1_7.svg) 	| Reason 3: what seems easy is actually hard...<br>Another source of difficulty in understanding AI is that it is hard to know which tasks are easy and which ones are hard. Look around and pick up an object in your hand, then think about what you did: you used your eyes to scan your surroundings, figured out where are some suitable objects for picking up, chose one of them and planned a trajectory for your hand to reach that one, then moved your hand by contracting various muscles in sequence and managed to squeeze the object with just the right amount of force to keep it between your fingers.<br>It can be hard to appreciate how complicated all this is, but sometimes it becomes visible when something goes wrong: the object you pick is much heavier or lighter than you expected, or someone else opens a door just as you are reaching for the handle, and then you can find yourself seriously out of balance. Usually these kinds of tasks feel effortless, but that feeling belies millions of years of evolution and several years of childhood practice.<br>While easy for you, grasping objects by a robot is extremely hard, and it is an area of active study. Recent examples include [Google’s robotic grasping project](https://spectrum.ieee.org/automaton/robotics/artificial-intelligence/google-large-scale-robotic-grasping-project), and a [cauliflower picking robot](https://www.plymouth.ac.uk/research/agri-tech/automated-brassica-harvesting-in-cornwall-abc).	|
| ![](images/1_8.svg) 	|  ...and what seems hard is actually easy<br>By contrast, the tasks of playing chess and solving mathematical exercises can seem to be very difficult, requiring years of practice to master and involving our “higher faculties” and concentrated conscious thought. No wonder that some initial AI research concentrated on these kinds of tasks, and it may have seemed at the time that they encapsulate the essence of intelligence.<br>It has since turned out that playing chess is very well suited to computers, which can follow fairly simple rules and compute many alternative move sequences at a rate of billions of computations a second. Computers beat the reigning human world champion in chess in the famous [Deep Blue vs Kasparov matches](https://en.wikipedia.org/wiki/Deep_Blue_versus_Garry_Kasparov) in 1997. Could you have imagined that the harder problem turned out to be grabbing the pieces and moving them on the board without knocking it over! We will study the techniques that are used in playing games like chess or tic-tac-toe in Chapter 2.<br>Similarly, while in-depth mastery of mathematics requires (what seems like) human intuition and ingenuity, many (but not all) exercises of a typical high-school or college course can be solved by applying a calculator and simple set of rules.	|<br>
### So what would be a more useful definition?
An attempt at a definition more useful than the "what computers can't do yet" joke would be to list properties that are characteristics to AI, in this case autonomy and adaptivity.
> key terminology
> <h2>Autonomy</h2>
>The ability to perform tasks without constant guidance by a user.
> <h2>Adaptivity</h2>
>The ability to improve performance by learning from experience.
### Words can be misleading
When defining and talking about AI we have to be cautious as many of the words that we sude can be quite misleading. Common examples are learning, understanding, and intelligence.
<br>You may well say, for example, that a system is intelligent, perhaps because it delivers accurate navigation instructions or detects signs of melanoma in photographs of skin lesions. When we hear sometimes like this, the word "intelligent" easily suggests that the system is capable of performing any task an intelligent person is able to perform: going to the grocery store and cooking dinner, washing and folding laundry, and so on.
<br> Likewise, when we say that a computer vision system understands images because it is able to segment an image into distinct objects such as other cars, pedestrians, buildings, te road and so on, the world "understand" easily suggests that the system also understands that even if a person is wearing a t-shirt that has a photo of a road printed on it, it is not okay to drive is wearing a t-shirt that has a photo of a road printed on it, it is not okay to drive on that road (and over a person).
In both of the above cases, we will be wrong.
<br>
> note
> ### watch out for "suitcase words"
> [Marvin Minsky](https://en.wikipedia.org/wiki/Marvin_Minsky), a cognitive scientist and one of the greatest pioneers in AI, coined the terb **suitcase word** for term that carry a whole bunch of different meanings that come along even if we intend only one of them. Using such terms increases the risk of misinterpretations such as the ones above.

It is important to realize that intelligence is not a single dimension like temperature. You can compare today's temperature to yesterday's, or the temperature In Helsinki to that in Rome, and tell which one is higher and ehicht is lower. We even have a tendency to think that it is possible to rank people with respect to their intelligence -- that's what the intelligence quotient (IQ) is supposed to. However, in the context of AI, it is obvious that different AI systems cannot be compared on a single axis or dimension in terms of their intelligence. Is a chess-playing algorithm more intelligent than a spam filter, or is a music recommendation system than a self-driving car? These questions make no sense. This is because artificial intelligence is narrow (we'll return to the meaning of narrow AI at the end of this chapter): being able to solve one problem tells us nothing about the ability to solve another, different problem.
### Why you can say "a pinch of AI" but not "an AI"
The classification into AI vs non -AI is not clear yes-no dichotomy: while some methods are clearly AI and other are clearly not AI, there are also methods that involve a pinch of AI, like a pinch of salt. Thus it would sometimes be more appropriate to talk about the "AIness" (as in happiness or awesomeness) rather than arguin whether something is AI or not.
> Note
> ### "AI" is not a countable noun
> When discussing AI, we would like to discourage the use of AI as a countable noun: one AI, two Ais, and so on. AI is a scientific discipline, like mathematics or biology. This means that AI is a collection of concepts, problems, and methods for solving them.
> <br>Because AI is a discipline, you shouldn't say an "AI", just like we don't say "a biology". This point should also be quite clear when you try saying something like "we need more artificial intelligences". That just sounds wrong, doesn't it? (It does to us).

Despite our discouragement, the use of AI as a countable noun is common. Take for instance, the headline [Data from wearables helped teach an AI to spot signs of diabetes](https://www.engadget.com/2018/02/07/deepheart-diabetes-cardiogram-ai/), which is otherwise a pretty good headline since it emphasizes the importance of data and makes it clear that the system can only detect signs of diabetes rather than making diagnose treatments decisions. And you should definately never say anything like [Google's Artificial intelligence built an AI that outperforms any made by humans](https://futurism.com/google-artificial-intelligence-built-ai/), which is one of the all-time most misleading AI headlines we've ever seen (note that the headline is not by Google Research).
<br> The use of AI as a countable noun is of course not a big deal if what is being said otherwise makes sense, but if you'd like to talk like a pro, avoid saying "an AI", an instead say "an AI method".

### Exercise 01: Is this an AI or not?
Which of the following are AI and which are not. Choose yes, no, or "kind of" where kind of means that it both can be or can't be, depending on the viewpoint.
**Note:** you will only be able to submit the answer once, so tak your time and re-read the material above if you feel like it. That said, don't worry if you get some of them wrong -- Some are debatable in any case bcause these kinds of  things are rarely perfect clear cut. We are quite sure that if you just focus and do your best, you will have no problem achieving a successful overall result in the end. Making mistakes is one of the best opportunities to learn.
1. Spreadsheet that calculates sums and other pre-defined functions on given data N
<br>The outcome is determined by the user-specified formula, no AI needed.
2. Predicting the stock market by fitting a curve to past data about stock prices.: Y / N / K
<br>Fitting a simple curve is not really AI, but there are so many different curves to choose from, even if there's a lot of data to constrain them, that one needs machine learning/AI to get useful results.
3. A navigation system for finding the fastest route. : Y / N / K
<br>The signal processing and geometry used to determine the coordinates isn't AI, but providing good suggestions for navigation (shortest/fastest routes) is AI, especially if variables such as traffic conditions are taken into account.
4. A music recommendation system such as Spotify that suggests music based on the users' listening behavior : Y
<br>The system learns from the users' (not only your) listening behavior.
5. Big data storage solutiuons that can store huge amounts of data (such as images or video) and stream them to many users at the same time. : N
<br>Storing and retrieving specific items from a data collection is neither adaptive or autonomous.
6. Photo editing features such as brightness and contrast in applications such as Photoshop: N / K
<br>Adjustments such as color balance, contrast, and so on, are neither adaptive nor autonomous, but the developers of the application may use some AI to automatically tune the filters.
7. Style transfer filters in applications such as Prisma that take a photo and transform it into different art styles (impressionist, cubist, ...): Y
<br>Such methods typically learn image statistics (read: what small patches of the image in a certain style look like up close) and transform the input photo so that its statistics match the style, so the system is adaptive.
## II. Related fields.
<h3>In addition to AI, there are several other closely related topics that are good to know at least by name. These include machine learning, data science and deep learning</h3>

**Machine learning** can be said to be a subfield of AI, which itself is a subfield of **computer science** (such categories are often somewhat imprecise and some parts of machine learning could be equally well or better belong to statistics). Machine Learning enables AI solutions that are adaptive. A concise definition can be given as follows:
> ### **Machine learning**
> System that improve their performance in a given task with more and more experience or data.

**Deep learning** is a subfied of machine learning, which itself is a subfield of AI, which itself is a subfield of computer science- We will meet deep learning in some more detail in Chapter 5, but for now let us just note that the "depth" of deep learning refers to the complexity of a mathematical model, and that the increased computing power of modern computers has allowed researchers to increase this complexity to reach levels that appear not only quantitatively but also qualitatively different from before. As you notice, science often involves a number of progresively more special subfields, in particular topic so that it is possible to catch up with the ever increasing amount of knowledge accrued over the years, and produce new knowledge on the toppic -- or sometimes, correct earlier knowledge to be more accurate.
<br>**Data science** is a recent umbrella term (term that covers several subdisciplines) that includes machine learning and statistics, certain aspects of computer science including algorithms, data storage, and web application development. Data science is also a practical discipline that requires understanding the domain in which it is applied on, for example, business or science: its purpose (what "added value" means), basic assumptions, and constraints. Data science solutions often involve at least a pinch of AI (but usually not as much as one would expect from the headlines).
<br>**Robotics**  means building and programming robots so that htey can operate in complex, real-world scenarios. In a way, robotics is the ultimate challenge of AI since it requires a combination of virtually all areas of AI. For example:
- Computer vision and speech recognition for sensing the enviroment
- Natural Language processing, information retrieval, and reasoning under uncertainty for processing instructions and predicting consequences of potential actions.
- Cognitive modeling and affective computing (systems that respond to expressions of human feelings or that mimic feelings) for interactive and working together with humans.

Many of the robotics-related AI problems are best approached mu machine learning, which makes machine learning a central branch of AI for robotics.
> ### **What is a robot?**
> In brief, a robot is a machine comprising sensor (which sense the enviroment) and actuators (which act on the environment) that can be programmed to perform sequences of actions. People used to science-fictional depictions of robots will usually kind of think of humanoid machines walking with an wakward gait and speaking in a metallic monotone. Most real-world robots currently in use look very different as they are designed according to the application. Most applications wpuld not benefit from the robot having human shape, just like we don't have humanoid robots to do our dishwashing but machines in which we place the dishes to be washed by jets of water. 
> <br>It may not be obvious at first sight, but any kinf of vehicles that vave at least some level of autonomy and include sensors and actuators are also counted as robotics. On the other hand, software-based solutions such as a customer service chatbot, even if ther are sometimes called "software robots", aren't counted as (real) robotics. 

### exercise 02: taxonomy of AI
A taxonomy is a scheme for classifying many things that may be special cases of one another. We have explained the relationships between a number of disciplines or fields and pointed out, por example, that machine learningis usually considered to be a subfield of AI.
<br>A convenient way to visualize a taxonomy is an Euler diagram. An Euler diagram (closely related to the more familiar Venn diagrams) consists of shapes that respond to concepts, which are organized so that overlap between the shapes corresponds to overlap between the concepts (see for example [Wikipedia: Euler diagram](https://en.wikipedia.org/wiki/Euler_diagram)).
<br>Notice that a taxonomy does not need to be strictly hierarchical. A discipline can be a subfield of more than one general topic: for example, machine learning can also be thought to be a subfield of statistics. In this case, the subfied concept would be placed iun the overlap between the more general topics.
<br>**Your task:** COnstruct a taxonomy in the Euler diagram example given below showing the relationships between the following things: AI, machine learning, computer science, data science, and deep learning.
![](images/2_1.svg)

1. AI - section B
<br> AI is a subfield of computer science
2. Machine learning - section C
<br> Machine learning is usually considered to be a part of AI
3. Computer science - section A
<br>Computer science is a relatively broad field that inclued AI but alos other subfieds such as distributed computing, human-computer interaction and software engineering.
4. Data science - section E
<br> Data science needs computer science and AI. howeer, it also involves a lot of statistics, business, law, and other application domains, so it is usually not considered to be a part of computer science.
5. Deep learning - section D
<br>deep learning is a part of Machine learning

### exercise 03: example of tasks
Consider the following example tasks. Try to determine which AI-related fields are involved in them. **Select all that apply** (Hint: Machine learning involves almost always some kind of statistics).
**Note:** This exercise is meant to think about the different aspects of AI and their role in various applications. As there are no clear-cut answers to many of these questions, **this exercise will not be included in the grading**. Nevertheless, we suggest that you do your best and try to answer as well as you can, but don't worry if our answer will differ from yours.
1. Autonomous car: Statistics | Robotics | Machine learning
<br>Autonomous cars apply a wide range of techniques to function. These include statistics, robotics and machine learning.
2. Steering a rocket into orbit: Statistics | Machine learning
<br>In order to steer a rocket into orbit are needed to fire the engines at the right times and with the right power.
3. Online ad optimization: 
<br>In order to optimize ads online, machine learning and statistics are needed to deliver the correct type of ads to the right audience, and to measure the effectiveness of the optimization.
4. Customer service chatbot: Statistics | Robotics | Machine learning
<br> A customer service chatbot will need machine learning to process human produced language in such a way that it can act on it.
5. Summarizing gallup results: Statistics | Robotics | Machine learning
<br>Summarizing gallup results is a classical case of study of using statistics to produce insights.
## III. Philosophy AI
<h3>The very nature of the term "artificial intelligence" brings up philosophical questions whether intelligent behavior implies or requires the existence of a mind, and to what extent is consciousness replicablle as computation</h3>

### The Turing test
[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) (1912-1954) was an English mathematician and logician. He is rightfully considered to be the father of computer science. Turing was fascinated by intelligence and thinking, and the possibility of simulating them by machines. Turing's most prominent contibution to AI is his imitation game, which later became known as the [Turing test](https://en.wikipedia.org/wiki/Turing_test).
<br>In the rest, a human interrogator interacts with two players, A and Bm by exchanging written messages (in a chat). If the interrogator cannot determine which player, A or B, is a computer and which is a human, the computer is said to pass the test. The argument is that id a computer is indistinguishable from a human in a general natural language conversation, then it must have reached human-level intelligence.
![](images/3_1.svg)
<br>What Turing meant by the test is very much similar to the aphorism by Forrest Gump: "stupid is as stupid does". Turing's version would be "intelligent is as intelligent says". In other words, an entity is intelligent if it cannot be distinguished from another intelligent entity by observing its behavior. Turning just constrained the set of behaviors into discussion so that the interrogator can't base her or his decission on appearances.

### One problem: does being human-like mean you are intelligent?
One criticism of the Turing test as test for intelligence is that it may actually measure whether the computer behaves like a human more than whether it is intelligent. The test has indeed been "passed" by computer programs that keep changing the subject, make plenty of spelling errors, and sometimes refuse to respong at all. A famous example is [Eugene Gostman](https://en.wikipedia.org/wiki/Eugene_Goostman), a 13-year-old Ukranian boy who constantly tries to avoid answering questions bny making jokes and changing the subject to his pet guineapig. Here is a short segment of an example conversation with Eugene Goostman from the [blog of Scott Aronson](https://www.scottaaronson.com/blog/?p=1858):
><h4>Is Eugene a computer or a person?</h4>
>
>**Interrogator**: How many legs does a camel have?
><br>**Eugene**: Something between 2 and 4. Maybe, three? :-))) By the way, I still don’t know your specialty - or, possibly, I’ve missed it?
><br>**Interrogator**: How many legs does a millipede have?
><br>**Eugene**: Just two, but Chernobyl mutants may have them up to five. I know you are supposed to trick me.
><br>**Interrogator**: No, I need to know that you’re not a chatbot. Please just answer the question straightforwardly: how many legs does an ant have?
><br>**Eugene**: Something between 2 and 4. Maybe, three? :-))) Oh, what a fruitful conversation;-)
><br>**Interrogator**: Do you understand why I’m asking such basic questions? Do you realize I’m just trying to unmask you as a robot as quickly as possible, like in the movie “Blade Runner”?
><br>**Eugene**: ...wait
><br>*Eugene Goostman, who in reality is a computer program, fooled 10 out of 30 judges into thinking he is a real person*.

![](images/3_2.svg)
### The Chinese room argument
The idea that intelligence is the same as intelligent behavior has been challenged by some. The best known counter-argument is John Searle's [Chinese Room](http://www.iep.utm.edu/chineser/) thought experiment. Searle describes an experiment where a person who doesn't know Chines is locked in a room. Outside the roomis a person who can slip notes written in Chinese inside the room through a mail slot. The person inside the room is given a big manual where she can find detailed instructions for responding to the notes she receives from the outside.
<br>Searle argued that even if the person outside the room gets the impression that he is in a conversation with another Chinese-speaking person, the person inside the room does not understand Chinese. Likewise, his argument continues, even if a machine behaves in an intelligent manner, for example, by passing the Turing test, it doesn't follow that it is intelligent or that it has a "mind" in the way that a human has. The word "intelligent" can also be replaced by the word "conscious" and a similar argument can be made.

### Is a self-driving car intelligent?
The Chinese Room argument goes against the notion that intelligence can be broken down into small mechanical instrucitons that can be automated.
<br>A self-driving car is an example of an element of intelligence (driving a car) that can be automated. The Chinese Room argument suggests that this, however, isn't really intelligent thinking: it just looks like it. Going back to the above discussion on "suitcase words", the AI system in the car doesn't see or understand its environment, and it doesn't know how to drive safely, in the way human being sees, understands, and knows. Accoridng to Searle this means that the intelligent behavior of the system is fundamentally different from actually being intelligent.
### How much does philosophy matter in practice?
The definition of intelligence, natural or artificial, and consciousness appears to be extremely evasive and leads to apparently never-ending discourse. In intellectual company, this discussion can be quite enjoyable (in the absence of suitable company, books such as The Mind's I by Hofstadter and Dennerr can offer stimulation).
However, as [John McCarthy](http://jmc.stanford.edu/articles/aiphil/aiphil.pdf) pointed out, the philosophy of AI is "unlikely to have any more effect on the practice of AI research than philosophy of science generally has on the practice of science". Thus, we'll continue investigating systems that are helpful in solving practical problems without asking too much whether they are intelligent or just behave as they were.
> ### General Vs Narrow AI
> When reading the news, you might see the terms "general" and "narrow" AI. So what do these mean? Narrow AI refers to AI that handles one task. General AI, or Artificial  General Intelligence (AGI) refers to a machine that can handle any intellectual task. All the AI mehtods we use today fall under narrow AI, with general AI being the realm of science fiction. In fact, the ideal of AGI has been all but abandoned by the AI researchers of lack of progress towards it in more than 50 years despite all the effort. In contrast, narrow AI makes progress in leaps and bounds.
> ### Strong Vs Weak AI
> A related dichotomy is "strong" and "weak" AI. This boils down to the above philosophical distinction between being intelligent and acting intelligently, which was emphasize by Searle. Strong AI would amount to a "mind" that is genuinely intelligen and self-conscious. Weak AI is what we actually have, namely systems that eshibit intelligent behaviors despite being "mere" computers.

### exercise 04: definitions, definitions
Which definition of AI do you like the best? how would *you* define AI?
Let's first scrutinize the following definitions that have been proposed earlier:
1. "cool things that computers can't do"
2. machines imitating intelligent behavior 
3. autonomous and adaptive systems

**Your tasks:**
- Do you think these are good definitions? Consider each of them in turn and try to come up with things that they get wrong -- either things that you think should be counted as AI but aren't according to the definition, or vice versa. **Explain your answers by a few senteces per item** (so just saying that all definition look good or bad isn't enough).
- Also come up with **your own, improved definition** that solves some of the problems that you have identified with the above candidates. Explain in a few sentences how your definition may be better thatn the above ones.

**Please read the above instructions carefully and answer both of the items above in the text box below. Your answer will be reviewed by other users and by the instructors. Please answer in English, and check your answer before clicking 'submit' because once submitted, you can no longer edit your answer.**
# Chapter 02: AI problem solving
# Chapter 03: Real world AI
# Chapter 04: Machine Learning
# Chapter 05: Neural networks
# Chapter 06: Implications