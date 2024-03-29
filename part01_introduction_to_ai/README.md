# Table of contents
[# chapter 01: what is ai](#chapter-01-what-is-ai)

[I. how should we define ai](#i-how-should-we-define-ai)
<br>[II. related fields](#ii-related-fields)
<br>[III. philosophy of ai](#iii-philosophy-ai)

[# chapter 02: ai problem solving](#chapter-02-ai-problem-solving)

[I. search and problem solving](#i-search-and-problem-solving)
<br>[II. solving problems with ai](#ii-solving-problems-with-ai)
<br>[III. search and games](#iii-search-and-games)

[# chapter 03: real world ai](#chapter-03-real-world-ai)

[I. odds and probability](#i-odds-and-probability)
<br>[II. the bayes rule](#ii-the-bayes-rule)
<br>[III. naive bayes rule](#iii-naive-bayes-classification)

[# chapter 04: machine learning](#chapter-04-machine-learning)

[I. The types of machine learning](#the-types-of-machine-learning)
<br>[II. The nearest neighbor classifier](#the-nearest-neighbor-classifier)
<br>[III. Regression](#regression)

[# chapter 05: neural networks](#chapter-05-neural-networks)

[I. Neural network basics](#i-neural-network-basics)
<br>[II. How neural networks are built](#ii-how-neural-networks-are-built)
<br>[III. Advanced neural network techniques](#iii-advanced-neural-network-techniques)

[# chapter 06: implications](#chapter-06-implications)

[I. About predicting the future](#i-about-predicting-the-future)
<br>[II. The societal implications of AI](#ii-the-societal-implications-of-ai)
<br>[III. Summary](#iii-summary)

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
- An AI is a way that a computer can answer to problems automatically, by no human interference. There are some tasks that they can manage to do, but some others like ethical decissions still cannot be accomplished byt the machine -- because the machine doesn't actually have a conscience, it just can solve efficiently a more logical task.
- As the machine imitates the human behavior, it gives the optimal answer to a specific question. If there's a new question, probably the machine won't answer as perfect as it did before because normally AI's are trained to do one specific task.
- AI is autonomous, because it "learns" by itself, and adapts to the different conditions that the problem may have. The thing is that at this point AI's are actually more narrow than they are general -- it's easier for the machine to give a more concrete answer to a concrete problem that have a general tool, that can generate different outputs for different problems.

There is no right or wrong answer, but here’s what we think:

“Cool things that computers can't do"

The good: this adapts to include new problems in the future, captures a wide range of AI such computer vision, natural language processing.

The bad: it rules out any "solved" problems, very hard to say what counts as "cool".

“Machines imitating intelligent human behavior”

The good: the same as in the previous. Also, imitate is a good word since it doesn't require that the AI solutions should "be" intelligent (whatever it means) and it's instead enough to act intelligently.

The bad: the definition is almost self-referential in that it immediately leads to the question what is 'intelligent', also this one is too narrow in the sense that it only includes human-like intelligent behavior and excludes other forms of intelligence such as so-called swarm intelligence (intelligence exhibited by for example ant colonies).

“Autonomous and adaptive systems”

The good: it highlights two main characteristics of AI, captures things like robots, self-driving cars, and so on, also nicely fits machine learning-based AI methods that adapt to the training data.

The bad: once again, these lead to further questions and the definition of 'autonomous' in particular isn't very clear (is a vacuum cleaner bot autonomous? How about a spam filter?). Furthermore, not all AI systems need to be autonomous and we can in fact often achieve much more by combining human and machine intelligence.
## Recap
<h3>After completing chapter 1, you whould be able to:</h3>

- Explain autonomy and adaptivity as key concepts for explaining AI
- Distingish between realistic and unrealistic AI (science fiction vs. real life)
- Express the basic philosophical problems related to AI including the implications of teh Turing test and Chinese room thought experiment.

# Chapter 02: AI problem solving
## I. Search and problem solving
<h3>Many problems can be phrased as searched problems. THis requires that we start by formulating the alternative choices and their consequences.</h3>

### Search in practice: getting from A to B
Imagine you're in a foreign city at some address (say a hotel) and want to use public transport to get to another adress (a nice restaurant, perhaps). What do you do? If you are like many people, you pull your smartphone, type in the destination and start following the instructions. 
<br>![](images/4_1.svg)
<br>This questions belongs to the class of search and planning problems. Similar problems need to be solved by self-driving cars, and (perhaps obviously) AI for playing games. In the game of chess, for example, the difficulty is not so much in getting a piece from A to B as keeping your pieces safe from opponent.
![](images/4_2.svg)
<br>Often there are many different ways to solve the problem, some which may be more preferable in terms of time, effort, cost or other criteria. Different search techniques may lead to different solutions, and developing advanced search algorithms is an established research area.
![](images/4_3.svg)
<br>We will not focus in the actual search algorithms. Instead, we emphasize the first stage of the problem solving process: defininf the choices and their consequences, which is often far from trivial and can require careful thinking. We also need to define what our goal is, or in other words, when we can consider the problem solved. After this has been done, we can look for a sequence of actions that leads from the initial state to the goal.
<br>In this chapter we will discuss two kinds of problems:
- Search and planning in static environments with only one "agent".
- Games with two-players ("agents") competiongn against each other.

These categories don't cover all possible real-world scenarios, but they are generic enough to demonstrate the main concepts and techniques.
<br>Before we address complex search tasks like navigation or playing chess, let us start from a much simplified model in order to build up our understanding of how we can solve problems by AI.
<br>![](images/4_4.svg)
### Toy problem: chicken crossing
We'll start from a simple puzzle to illustrate the ideas. A robot on a rowboat needs to move three pieces of cargo accross a river: a fox, a chicken and a sack of chicken-feed. The fox will eat the chicken if it has the chance, and the chicken will eat the chicken-feed if it has the chance, and neither is a desirable outcome. The robot is capable of keeing the animas from going harm when it is near them, but only the robot can operate the rowboat and only teo of the pieces of cargo can fit on the rowboat together with the robot. How can the robot move all of its cargo to the opposite bank of the river?
> <h3>The easy version of the rowboat puzzle</h3>
>If you have heard this riddle before, you might know that it can be solved even with less space on the boat. That will be an exercise for you after we solve this easier.
<br>We will model the puzzle by nothing that five movable things have been identified: the robot, the rowboat, the fox, the chicken, and the chicken-feed. In principle, each of the five can be on either side of the river, but since only the robot can operate the rowboat, the two will always be on the same side. Thus there are four things with two possible positions for each, which makes for sixteen combinations, which we will call states:
<h3>States of the chicken crossing puzzle</h3>

| State 	| Robot 	| Fox 	| Chicken 	| Chicken-feed 	|
|---	|---	|---	|---	|---	|
| NNNN 	| Near side 	| Near side 	| Near side 	| Near side 	|
| NNNF 	| Near side 	| Near side 	| Near side 	| Far side 	|
| NNFN 	| Near side 	| Near side 	| Far side 	| Near side 	|
| NNFF 	| Near side 	| Near side 	| Far side 	| Far side 	|
| NFNN 	| Near side 	| Far side 	| Near side 	| Near side 	|
| NFNF 	| Near side 	| Far side 	| Near side 	| Far side 	|
| NFFN 	| Near side 	| Far side 	| Far side 	| Near side 	|
| NFFF 	| Near side 	| Far side 	| Far side 	| Far side 	|
| FNNN 	| Far side 	| Near side 	| Near side 	| Near side 	|
| FNNF 	| Far side 	| Near side 	| Near side 	| Far side 	|
| FNFN 	| Far side 	| Near side 	| Far side 	| Near side 	|
| FNFF 	| Far side 	| Near side 	| Far side 	| Far side 	|
| FFNN 	| Far side 	| Far side 	| Near side 	| Near side 	|
| FFNF 	| Far side 	| Far side 	| Far side 	| Far side 	|
| FFFN 	| Far side 	| Far side 	| Far side 	| Far side 	|
| FFFF 	| Far side 	| Far side 	| Far side 	| Far side 	|

We have given short names to the states, because otherwise it would be cumbersome to talk about them. Now we can say that the starting state is NNNN and the goal state is FFFF, instead od something like "in the starting state, the robot is on the near side, the foz is on the near side, the chicken is on the near side, and also the chicken-feed is on the near-side", and so on.
<br>Some of these are forbidden by the puzzle conditions. For example, in state NFFN (meaning that the robot is on the near side, with the chicken-feed byt the fox and the chicken are on the far side), the fox will eat the chicken, which we cannot have. Thus we can rule out states `NFFN`, `NFFF`, `FNNF`, `FNNN`, `NNFF`, and `FFNN` (you can check each one if you doubt ourreasoning). We are left with the following ten states:

| State 	| Robot 	| Fox 	| Chicken 	| Chicken-feed 	|
|---	|---	|---	|---	|---	|
| NNNN 	| Near side 	| Near side 	| Near side 	| Near side 	|
| NNNF 	| Near side 	| Near side 	| Near side 	| Far side 	|
| NNFN 	| Near side 	| Near side 	| Far side 	| Near side 	|
| NFNN 	| Near side 	| Far side 	| Near side 	| Near side 	|
| NFNF 	| Near side 	| Far side 	| Near side 	| Far side 	|
| FNFN 	| Far side 	| Near side 	| Far side 	| Near side 	|
| FNFF 	| Far side 	| Near side 	| Far side 	| Far side 	|
| FFNF 	| Far side 	| Far side 	| Near side 	| Far side 	|
| FFFN 	| Far side 	| Far side 	| Far side 	| Near side 	|
| FFFF 	| Far side 	| Far side 	| Far side 	| Far side 	|

Next we will figure out which state transitions are possible, meaning simply that as the robot rows the boat with some of the items as cargo, what the resulting state in each case. It's best to draw a diagram of the transitions, and since any transition the first letter alternates between N and F, it is convenient to draw the states starting with N (so the robot is on the near side) in one row and the states starting with F in another row:
<br>![](images/4_5.svg)
<br>Now let's draw the transitions. We could draw arrows that have a direction so that they point from one node to another, but in this puzzle the transitions are symmetric: if the robot can row state `NNNN` to state `FNFF`, it can equally well row the other way from `FNFF` to `NNNN`. Thus is simpler to draw the transitions simply with lines that don't have lines that don't have a direction. Starting from `NNNN`, we can go to `FNFF`, `FNFN`, `FNFF`, and `FFFN`:
<br>![](images/4_6.svg)
<br>Then we will fill in the rest:
<br>![](images/4_7.svg)
<br>We have done quite a bit of work on the puzzle without seeming any closer to the solution, and ther is little doubt that you could have solved the whole puzzle already by using your "natural intelligence". But for more complex problems, where the number of possible solutions grows in the thousands and in the millions, our systematic or mechanical approach will shine since the hard part will be suitable for a simple computer to do. Now that we have formulated the alternative states and transitions between them, the rest becomes a mechanical task: find a path fro mthe initial state `NNNN` to the final state `FFFF`.
<br>One such path is colored in the following picture. The path proceeds from `NNNN` to `FFFN` (the robot takes the fox and the chicken to the other side), thence to `NFNN` (the robot takes the chicken back on the starting side) and finally to `FFFF` (the robot can now move the chicken and the chicken-feed to the other side).
<br>![](images/4_8.svg)
### State space, transitions, and costs
To formalize a planning problem, we use concepts such as the state space, transitions, and costs.
> <h3>The state space</h3>
>means the set of posible situations. In the chicken-crossing puzzle, the state space consisted of ten allowed states `NNNN` trough to `FFFF` (but not for example `NFFF`, which the puzzle rules don't allow). If the task is to navigate from place A to place B, the state space could be the set of locations defined by their (x, y) coordinates that can be reached from the starting point A. Or we could use a constrained set of locations, for example, different street addresses so that the number of possible states is limited.
><h3>Transitions</h3>
>are possible moves between one state and another, such as `NNNN` to `FNFN`. It is important to note that we only count direct transitions that can be accomplished with a single action as transitions. A sequence of multiple transitions, for example, from A to C, from C to D, and from D to B (the goal), is a path rather than a transition.
><h3>Costs</h3>
>refer to the fact that, oftentimes the different transitions aren't all alike. They can differ in ways that make some transitions more preferable or cheaper (in a not necessarily monetary sense of the word) and others more constly. We can express this by associating with each transition a certain cost. If the goal is to minimize the total distance traveled, then a natural cost is the geographical distance between states. On the other hand, the goal could actually be to minimize the time instead of the distance, in which case the natural cost would obviously be the time. If all the transations are equal, then we can ignore the costs.
### exercise05: A smaller rowboat
In the traditional version of this puzzle the robot can only fit one thing on the boat with it. The state space is still the same, but fewer transitions are possible.
<br>**Using the diagram with the possible states below as a starting point, draw the possible transitions to it** (it is MUCH easier to do this with a pen and paper than without).
<br>Having drawn the state transition diagram, **find the shortest path from NNNN to FFFF, and calculate the number of transitions on it**.
<br>Please type your answer s the **number of transitions in the shortest path** (just as a sible number like "12"). Hint: do *not* count the number od states, but the number of transitions. For example, the number of transitions in the path `NNNN`->`FFNF`->`NFNF`->`FFFF` is *3* instead of 4.
<br>![](images/4_9.svg)
>The correct answer is 7. There are two shortest paths that lead from the start `NNNN` to the goal `FFFF`. One of them is `NNNN` -> `FNFN` -> `NNFN` -> `FFFN` -> `NFNN` -> `FFNF` -> `NFNF` -> `FFFF`, and the other `NNNN` -> `FNFN` -> `NNFN` -> `FNFF` -> `NNNF` -> `FFNF` -> `NFNF` -> `FFFF`. Intuitively, the strategy is to move the chicken on the other side first, and then go back get either the fox or the feed, and take it to the far side too. The robot then takes the chicken back to the near side to save it from being eaten or from eating the feed, and takes the other remaining object (fox or feed) from the near side to the far side. Finally, the robot goes to fetch the chicken and takes it to the far side to reach the goal.
### exercise06: the towers of Hanoi
Let's do another puzzle: the well-known [Towers of Hanoi](https://www.britannica.com/topic/Tower-of-Hanoi). In our version, the puzzle involves three pegs, and two discs: one large, and one small (actually, there can be any number of discs but the exercise, two is enough to demonstrate the principle).
<br>In the initial state, both discs are stacked in the first (leftmost) peg. The goal is to move the discs to the third peg. You can move one disc at a time, from any pe to another, as long as there is no other disc on top of it. It is not allowed to put a larger disc on top of a smaller disct.
<br>This picture shows the initial state and the ogal state. There are also seven other states so that the total number of possible states in nine: three ways to place the large disc and for each of them, three was to place the small disc.
<br>![](images/4_10.svg)
<br>**Your task**: Draw the state diagram. The diagram should include all the nine possible states in the game, connected by lines that show the possible transitions. The pictures below shows the overall structure of the state diagram and the positions of the first three states. It shows that from the starting state (at the top corner), you can move to two other states by moving the small disc. Complete the state diagram by placing the remainig states in the correct places. Note that the transitions are again symmetric and you can also move sideways (left or right) or up in the diagram.
<br>After solving the task using pen and paper, enter your solution by choosing which state belongs to which node in the diagram. (Hint: each state belongs to exactly one node).
<br>![](images/4_11.svg)
<br>**Choose for each node (1-6 in the above diagram the correct state A-F from below**
<br>![](images/4_12.svg)
- box1: State E is the only option that is reachable from the left box on the second row.
- box2: Since box 1 contains state E, there are two possibilities for box 2: states B and F. Choosing state F in box 2 would lead to a dead-end at box 5, so the correct option must be state B. Also note that box 2 has two transitions to other states, which implies that it must be a state where the two discs are on top of each other.
- box3: Since box 1 contains state E, there are two possibilities for box 3: states B and F. Choosing state B would lead to a dead end in box 5, so the correct choice must be state F.
- box4: State D is the only option that is reachable from the right box on the second row.
- box5: Since box 4 contains state D, there are two possibilities for box 5: states A and C. Choosing state A would lead to a dead end in box 3, so the correct choice must be state C.
- box6: Since box 4 contains state D, there are two possibilities for box 6: states A and C. Choosing state C would lead to a dead end in box 5, so the correct choice must be state A. Also note that box 6 has two transitions to other states, which implies that it must be a state where the two discs are on top of each other.

## II. Solving problems with AI
### Interlude on the story of AI: starting from search
AI is arguably as old as computer science. Long before we had computers, people thought of the possibility of automatic reasoning and intelligence. As we already mentioned in [chapter 1](#chapter-1), one of the great thinkers who considered this question was Alan Turing. In addition to the Turing test, his contributions to AI, and more generally to computer science, include the insight that anything that can be computed (= calculated using either numbers or other symbols) can be automated.
> ### Helping win WWII
><br> Turing designed a very simple devcie that can compute anything that is computable. His device is known as the Turing machine. While it is a theoretical model that isn't practically useful, it lead Turing to the invention of programmable computers: computers that can be used to carry out different tasks depending on what they were programmed to do.
><br>So instead of having to build a different device for each task, we use the same computer for many tasks. This is the idea of programming. Today its invention sounds trivial but in Turing's days it was far from it. Some of the early programmable computers were used during World War II to crack German secret codes, a project where Turing was also personally involved.

The term Artificial Intelligence was coined by John McCarthy (1927-2011) - who was refered as the father of AI. The term became stablished when it was chosen as the topic of a summer seminar, known as the [Darmouth conference](https://en.wikipedia.org/wiki/Dartmouth_workshop), which was organized by McCarthy and others in 1956 at Dartmouth college in New Hampshire. In the proposal to organize the seminar, McCarthy continued with Turing's argument about automated computation. The proposal contains the following crucial statement:
><h3>John McCarthy key statement about AI</h3>
><br>"The study is to proceed on the basus of the conjeture that every aspect of learning or any other feature of intelligence can in principle be so precisely described that a machine can be made to simulate it."

In other words, any element of intelligence can be broken down into small steps so that each of the steps is a such so simple and "mechanical" that it can be written down as a computer program. This statement was, and is still today, a conjeture, which means that we can't really prove it to be true. Nevertheless, the idea is absolutely fundamental when it comes to the way we think about AI.
For example, it shows that McCarthy wanted to bypass any arguments in the spirit of Searle's Chinese Room: intelligence is intelligence even if the system that implements it is just a computer that mechanically follows a program.
### Why search and games became central in AI research
As computers developed to the level where it was feasible to experiment with practical AI algorithms in the 1950s, the most distinctive AI problems (besides cracking Nazi codes) were games. Games provided a convenient restricted domain that could be formalized easily. Board games such as checkers, chess, and recently quite predominently Go (an extremely complex strategy board game originating from China at leas 2500 years ago), have inspired countless researchers, and continue to do so.
<br>Closely related to games, search and planning techniques were an are where AO led to great advances in the 1960s: algorithms with names such as the Minimax algorithm or Alpha-Beta Pruning, which were developed then, are still the basis for game playing AI, although of course more advanced variants have been proposed over the years. In this capter, we will study games and planning problems on a conceptual level.
## III. Search and games
<h4>In this section, we will study a classic AI problem: games. The simplest scenario, which we will focus on for the sake of clarity, are two-player, perfect-information games such as tic-tac-toe and chess.</h4>

### Example: playing tic tac toe
Maxine and Minnie are true game enthusiasts. THey just love games. Especially two-person, perfect information games such as tic-tac-toe or chess. One day they were playing tic-tac-toe. Maxine, or Max, as her friends call her, was playing with X. Minnie, or Min as her friends call her, had the Os. Min had just played her turn and the board looked as follows:
<br>![](images/5_1.svg)
<br>Max was looking at the board and contemplating her next move, as it was her turn, when she suddenly buried her face in her hands in despai, looking quite like Garry Kasparov playing Deep Blue in 1997.
<br>Yes, Min was close to getting three Os on the top row, but Max could easily put a stop to that plan. So why was Max so pesimistic?
### Game trees
To solve games using AI, we will intoduce the concept of a game tree. The different states of the game are represented by nodes in the game tree, very similar to the above planning problems. The idea is just slightly differnet. In the game tree, the nodes are arranged in levels that correspond to each player's turns in the game so that the "root" node of the tree (usually depicted at the top of the diagram) is the beginning position in the game. In tic-tac-toe, this would be the empty grid with no Xs or Os played yet. Under root, on the second level, there are the possible states that can result from the fist player's moves, be it X or O. We call these nodes the "children" of the root node.
<br>Each node on the second level, would further have as its children nodes the states that can be reached from it by the opposing player's moves. This is continued, level by level, until reaching states where the game is over. In tic-tac-toe, this means that either one of the players gets a line of three and wins, or the board is full and the game ends in a tie.
### Minimizing and Maximizing value
In order to be able to create game AI that attempts to win the game, we attach a numerical value to each possible end result. To the board positions where X has a line of three so that Max wins, we attach the value +1, and likewise, to the position where min wins with three Os in a row we attach the value -1. For the positions where the board is full and neither player wins, we use the neutral value 0 (it doesn't really matter what the values are as long as they are in this order so that Max tries to maximize the value, and Min tries to minimize it).
#### A sample game tree
Consider, for example, the following game tree which begins not at the root but in the middle of the game (because otherwise, the tree would be way too big to dsiplay). Note that this is different from the game shown in the illustration in the beginning of this section. We have numbered the nodes with numbers 1, 2, ..., 14.
<br>The tree is composed of alternating layers where it is either Min's turn to place an O or Max's turn to place an X at any of the vacant slots on the board. THe player whose turn it is to play next is shown at the left.
<br>![](images/5_2.svg)
<br>The game continues at the board position shown in the root node, numbered as (1) at the top, with Min's turn to place O at any of the three vacant cells. Nodes (2)-(4)  show the board positions resulting from each of the three choices respectively. In the next step, each node has two possible choices for Max to play X each, and so the tree branches again.
<br>When starting from the above starting position, the game always ends in a row of three: in nodes (7) and (9), the winner is Max who plays with X,and in nodes (11)-(14) the winner is Min who plays with O.
<br>Note that since the players' turn alternate, the levels can be labeled as Min levels and Max levels, which indicate whose turn it is.
### Being stategic
<br>Consider nodes (5)-(10) on the second level from the bottom. In nodes (7) and (9), the game is over, and Max wins with three X's in a row. The value of these positions is +1. In the remaining nodes (5), (6), (8) and (10), the game is also practically over, since Min only needs to place her O in the only remaining cell to win. In other words, we know how the game will end at each node on the second level from the bottom. We can therefore decide that the value of nodes (5), (6), (8) and (10) is also -1.
<br>![](images/5_3.svg)
<br>Here comes the interesting part. Let's consider the values of the nodes one level higher towards the root: nodes (2)-(4). Since we observed that both of thechildren of (2), i.e., nodes (5) and (6), lead to Min0s victory, we can without hesitation attach the value -1 to node (2) as well. However, for node (3), the left child (7) leads to Max's victory, +1, but the right child (8) leads to Min winning, -1. What is the valye of node (3)? Think about this for a while, keeping in mind who makes the coice at node (3).
<br>Since it is Max's turn to play, she will of course choose the left child, node (7). Thus, every time we reach the board position in node (3), Max can ensure victory, and we can attach the value +1 to node (3).
<br>The same holds for node (4): again, since Max can choose where to put her X, she can always ensure victory, and we attach the value +1 to node (4).
<br>![](images/5_4.svg)
### Determining who wins
<br>The most important lesson in this section is to apply the above kind of reasoning repeatedly to determine the result of the game in advance from any board position.
<br>So far, we have decided that the value of node (2) is -1, which means that if we end up in such a board position, Min can ensure winning, and that the reverse holds for nodes (3) and (4): their value is +1, which means that Max can be sure to win if she only plays her own turn wisely.
<br>Finally, we can deduce that since Min is an experienced player, she can reach the same conclusion, and thus she only has one real option: play the O in the middle of the board.
<br>In the diagram below, we have included the value of each node as well as the optimal game play starting at Min's turn in the root node.
<br>![](images/5_5.svg)
### The value of the root node = who wins
<br>The value of the root node, which is said to be the value od the game, tells uys who wins (and how much, if the outcome is not just win or lose): Max wins if the value of the game is +1, Min if the value is -1, and if the value is 0, then the game will end in a draw. In other games, the value may also take other values (such as the monetary value of the chips in front of you in poker for example).
<br>This all is based on the assumption that both players choose what is best for them and that what is best for one is the worst for the other (so called "zero-sum game").
> <h3>Finding the optimal moves</h3>
> Having determined the values of all the nodes in the game tree, the optimal moves can be deduced: at any Min node (where it is Min's turn), the optimal choice is given by the child node whose value is minimal, and conversely, at any Max node (where it is Max's turn), the optimal choice is given by the child node whose value is maximal. Sometimes there are many equally good choices that are, well, equally good, and the outcome willl be the same no matter which one of them is picked.
### The Minimax algoithm
We can exploit the above concept of the value of the game to obtain an algorithm called the Minimax algorithm. It guarantees optimal game play in, theretically speaking, any deterministic, two-person, perfect-information zero-sum game. Given the state of the game, the algorithm simply computes the values of the children of the given state and chooses the one that has the maximum value if it is Max's turn, and the one that has the minimum value if it is Min's turn.
<br>The algorithm can be implemented using a few lines of code. However, er will be satisfied with having grasped the main idea. If you are interested in taking a look at the actual algorithm (alert: programming required) feel free to check out, for example, [Wikipedia: Minimax](https://en.wikipedia.org/wiki/Minimax#Minimax_algorithm_with_alternate_moves).
![](images/5_6.svg)
### COunds good, can I go home now?
As stated above, the Minimax can be used to implement optimal game play in any deterministic, two-player, perfect-informtion zero-sum game. Such games include tic-tac-toe, connect four, Go, etc. Rock-paper-scissors is not in this class of games since it involves information hidden from the other player; nor are Monopoly or backgammon which are not deterministic. So far as this topic is concerned, is that all folks, can we go home now? The answer is that in theory, yes, but in practice, no.
> <h3>The problem of massive game trees</h3>
> In many games, the game tree is simply way too big to traverse in full. For example, in chess the avarage branching factor, i.e., the average number of children (available moves) per node is about 35. That means that to explore all the possible scenarios up to only two moves ahead, we need to visit approximately 35 x 35 = 1225 nodes - probably not your favorite pencil-and-paper homework exercise. A look-ahead of three moves requires visiting 42875 nodes; four moves 1500625; and ten moves 2758547353515625 (that’s about 2.7 quadrillion) nodes. In Go, the average branching factor is estimated to be about 250. Go means no-go for Minimax.
### More tricks: Managing massive game trees
A few more tricks are needed to manage massive game trees. Many of them were crucial elements in IBM's Deep Blue computer defeating the chess world champion Garry Kasparov in 1997.
<br>If we can afford to explore only a small part of the game tree, we need a way to stop the Minimax algorithm before reaching an end-node, i.e., a node where the game is over and the winner is known. This is achieved by using a so called **heuristic evaluation function** that takes as input a board position,m including the information about which player's turn is next, and returns a score that should be an estimate of the likely outcome of the game continuing from the given board position.
> <h3>Good heuristics</h3>
>Good heuristics for chess, for example, typically count the amount of material (pieces) wighted by their type: the queen is usually considered worth about two times as much as a rook, three times a knight or a bishop, and nine times as much as a pawn. The king is of course worth more than all other things combined since losing it amounts to losing the game. Further, occupying the strategicaly important positions near the middle of the board is considered an advantage and the heuristics assign higher value to such positions.

The Minimax algorithm presented above requiers minimal changes to obtain a **depth-limited** version where the heuristic ius returned at all nodes at a given depth limit: the depth simply refers to the number of steps that the game is expanded before applying a heuristic evaluation funcion.
### exercise07: why so pessimistic, Max?
Let's return to the tic-tac-toe game described in the beginning of this section. To narrow down the space of possible end-games to consider, we can observe that Max must clearly place an X on the top row to avoid imminent defeat:
<br>![](images/5_7.svg)
<br>Now it's Min's trun to play an O. Evaluate the value of this state of the game as well as the other states in the game tree where the above psition is the root, using the Minimaz algorithm.
<br>**Your task**:
<br>Look at tge game tree starting from the below board position. Using a pencil and paper, fill in the values of the bottom-level nodes where the game is over. Note that this time some of the games end in a draw, which means that the values of the node is 0 (instead of -1 or 1).
<br>Next continue filling the values of the nodes in the next level up. Since there is no branching at that level, the values on the second-lowest level are the same as at the bottom level.
<br>On the second-highest level, fill in the values by choosing for each node the maximum of the values of the child nodes - as you notice, this is a MAX level. Finally, fill in the root node's value by choosing the minimum of the root node's child nodes' values. This is the value of the game.
<br>**Enter the value of the game as your answer**.
<br>![](images/5_8.svg)
<br>The value is –1. The values on the second level are 0, 0, and –1. The values on the third level are –1, 0, –1, 0, –1, –1, which are the same as the values on the bottom level. As you can see, Max has all the reason to be serious since by playing in the bottom-right corner, Min can guarantee a win. The inevitable victory of Min can also be seen from the value of the game –1.
><h3>The limitations of plain search</h3>
>It may look like we have a method to solve any problem by specifying the states and transitions between them, and finding a path from the current state of our goal. Alas, things get more complicated when we want to apply AI in real world problems. Basically, the number of states in even a moderately complex real-world scenario grows out of hand, and we can't find a solution by exhaustive search ("brute force") or even by using clever heuristics.
><br>Moreover, the transitions which take us from one state to the next when we choose an action are not deterministic. This means that whatever we choose to do will not always completely determine the outcome because there are factors that are beyond our control, and that are often unknown to us.
><br>The algorithms we have discussed above can be adapted to handle some randomness, for example randomness in choosing cards from a shuffled deck or throwing dice. This means that we will need to introduce the concept of uncertaintiy and probability. Only thus we can begin to approach real-world AI instead of simple puzzles and games. This is the topic of Chapter 3.
## Recap
- Formulate a real-world problem as a search problem.
- Formulate a simple game (such as tic-tac-toe) as a game tree
- Use the minimax principle to find optimal moves in a limited-soze game tree

# Chapter 03: Real world AI
## I. Odds and probability
<h3>In the previous section, we discussed search and its application where there is perfect information - such as in games like chess. However, in the real world things are rarely so clear out.</h3>
Instead of perfect information, there is a host of unknown possibilites, ranging from missing information to deliberate deception.
<br>Take a self-driving car for example - you can set the goal to get from A to B in an eficient and saf manner that follows all laws. But what happens if the raffic gets worse than expected, maybe because of an accident ahead? Sudden bad weather? Random events like a ball bouncing in the street, or a piece of trash flying straight into the car's camera?

<br>![](images/6_1.svg)
<br>A self driving car needs to use a variety of sensors, including solar-like ones and cameras, to detect where it is and what is around it. These sensors are never perfect as the data from the sensors always includes some errors and inaccuracies called "noise". It is very common then that one sensor indicates that the road ahead turns left, but another sensor indicates the opposite direction. This needs to be resolved without always stopping the car in case of even a slightest amount of noise.
### Probability
One of the reasons why modern AI methods actually works in real-world problems - as opposed to most of the earlier "good old-fashioned" methods in the 1960-1980s - is their anility to deal with uncertainty.
><h3>The history of dealing with uncertainty</h3>
>The history of AI has seen various competing paradigms for handling uncertain and imprecise information. For example, you may have heard of fuzzy logic. Fuzzy logic was for a while a contender for the best approach to handle uncertain and imprecise information and used in many customer-applications such as washing machines where the machine could detect the dirtiness (a matter of degrees, not only dirty or clean) and adjust the program accordingly.
><br>However, probability has turned out to be the best approach for reasoning under uncertainty, and almost all current AI applications are based, to at least some degree, on probabilities.
<br>![](images/6_2.svg)
### Why probability matters
We are perhaps most familiar with applications of probability in games: what are the chances of getting three of a kind in poker (about 1 in 47), what are the chances of winning in the lottery (very small), and so on. However, far more importantly, probability can also be used to quantify and compare risks in everyday life: what are the chancs of crashing your car if you exceed the speed limit, what are the chances that the interest rates on your mortgages will go up by five percentage points within the next five years, or what are the chances that AI will automate particular tasks such as detecting fractured bones in X-ray images or wating tables in a restaurant.
><h3>The key lesson about probability</h3>
>The most important lesson about probability that we'd like to take away is not probability calculus. Instead, it is the ability to think that we can talk about uncertainty as if it were a number: numbers can be compared ("is this thing more probable than that thing"), and they can often be measured.
><br>Granted, measuring probabilities is hard: we usually need many observations about a phenomenon to draw conclusions. However, by systematically collecting data, we can critically evaluate probabilistic statements, and our numbers can sometimes be found to be right or wrong. In other words, the key lesson is that uncertainty is not beyond the scope of rational thinking and discussion, and probability provides a sustematic way of doing just that.
<br>The fact that uncertainty can be qualified is a paramount importance, for example, in decisions concerning vaccination or other public policies. Before entering the market, any vaccine are never knwon to the minutest detail, but their magnitude is usually known to sufficient degree that it can be argued whether the benefits outweight the risks.
><h3>Why quantifying uncertainty matters</h3>
>if we think of unmcertainty as somethin that can't be qua, the uncertainty aspect may become an obstacle for rational discussion. We may for example argue that since we don't know exactly whether a vaccine may cause a harmful side-effect, it is too dangerous to use. However, this may lead us to ignore a life-threatening disease that the vaccine will eradicate. In most cases, the benefits and risks are known to sufficient precission to clearly see that one is more significant then the other.
<br>The above lesson is useful in many everyday scenarios and profesinally: for example, medical doctors, judges in a court of law, or investors have to process uncertain information and make rational decidions based on them. Since this is an AI course, we will discuss how probability can be used to automate uncertain reasoning. The examples we will use include medical diagnosis (although it is usually not a task that we'd wish to fully automate), and identifying fraudulent email messages ("spam").
### exercise08: probabilistic forecast
For this exercise, remember the key points from the above discussion: probability can be quantified (expressed as a number) and it can be right or wrong. But also keep in mind, that it is usually not possible to draw conclusions about wheter a particular number was right or wrong based on a single observation.
<br>Consider the following four probabilisitc forecast and outcomes. What can we conclude based on the outcome about the correctness od the forecasts? Can we conclude that the probability given by the forecast was indeed **the** correct probability (choose "right"), taht hte forecast was worng (choose "wrong"), or can we conclude neither way (choose "cannot be concluded")?
- The weather forecast says it's going to rain with 90% probability tomorrow but the day turns out to be all sun and no rain. -- cannot be concluded.
<br>We can't conclude that the weather forecast was wrong based on only the single event. The forecast said it's going to rain with 90% probability, which means it would not rain with 10% probability or in one out of 10 days. It is perfectly plausible that the day in question was the 1 in 10 event. Concluding that the probability 90% was correct would also be wrong because by the same argument, we could then conclude that 80% chance of rain was also correct, and both cannot be correct at the same time.
- The weather forecast says it's going to rain with 0% probability tomorrow but the day turns out to be rainy. - wrong
<br>The weather forecast was wrong because a 0% probability means that it should definitely not rain. But it did.
- Suppose you monitor a weather forecaster for a long time. You only consider the days for which the forecast gives 80% chance of rain. You find that in the long run, on the average it rains on three out of every five days. - Wrong.
<br>The weather forecasts are wrong if they predict 80% chance of rain and it rains only 60% (three out of five) of the time in the long run. (Note that we'd really need to keep track of the accuracy for a long time to reach this conclusion but that's what "in the long run" means.) In practice, weather forecasters actually tend to provide this kind of 'wrong' predictions just to be safe: people are often quite disappointed when the weather turns out to be worse than predicted but pleasantly surprised when it turns out better than predicted.
-In the United States presidential election 2016, a well-known political forecast blog, Five-Thirty-Eight, gave Clinton a 71.4% chance of winning (vs Trump's 28.6%). However, contrary to the prediction, Donald Trump was elected the 45th president of the United States.
<br>Cannot be concluded to be wrong (or right). Sometimes unlikely things happen. Considering the previous item, it would actually have been wrong to predict, say, 90% or 100% chance for Trump if there simply isn't enough information available to anticipate the outcome. In other words, perhaps Trump's victory was a rare (or rareish) event with 28.6% probability. Such events are expected to happen in more than one out of four cases, after all.
### Odds
Probably the easiest way to represent uncertainty is through odds. They make it particularly easy to update beliefs when more information becomes available (we will return to this in the next section).
<br>Before we proceed any further, we should make sure you are comfortable with doing basics manipulations on ratios (or fractions). As you probably recall, fractions are numbers like 3/4 pr 21/365. We will need tp mulstiply and divide such things, so it's good to refresh these operations if you fell unsure about them. A compact presentation for those who just need a quick reminder is [Wikibooks: Multiplying fractions](https://en.wikibooks.org/wiki/Arithmetic/Multiplying_Fractions). Another fun animated presentation of the basic operations is [Math is Fun: Using rational numbers](https://www.mathsisfun.com/algebra/rational-numbers-operations.html). Feel free to consult our favorite source if necessary.
<br>By odds, we mean an expression like 3:1 (three to one), which means that we wxpect that for every three cases of an outcome, for example winning a bet, there is one case of the opposite outcome, not winning the bet. (In gambling terms, the odds are usually given from the bookmakers point of view, so 3:1 usually means that *your* chances of winning are 1:3). The other way to express way to express the same would be to say that the chances of winning 3/4 (three in four). These are called natural frequencies since they involve only whole numbers. With whole numbers, it is easy to imagine, for example, four people out of whom, three have brown eyes. Or four days out of which it rains on three (if you're in Helsinki).
<br>![](images/6_3.svg)
><h3>Why we use odds and not percentages</h3>
>Three out of four is of course the same as 75% (mathematicians prefer to use fractions like 0.75 instead of percentages). It has been found that people get confused and make mistakes more easily when dialing with fractions and percentages than with natural frequencis or odds. THis is why we use natural frequencies and adds whenever convenient.

An important thing to notice is that while expressed as two numbers, 3 and 1, for example, the odds can actually be thought of as single fraction or a ratio, for example 3/1 (three divided by one) which is equal to 3. THus, the odds 3:1 is the same as the ofdds 6:2 or 30:10 since these ratios are also equals to 3. Likewise, the odds 1:5 can be thought as 1/5 (one divided by 5) which equals 0.2. Again, this is the same as the odds 2:10 or 10:50 because that's what you get dividing 2 by 10 or 10 by 50. But be very careful! The odds 1:5 (one win for every five losses), even if it can be expressed as the decimal number 0.2, is differenct from 20% probability (or probability 0.2 using the mathematicians' notation). The odds 1:5 mean that you'd have to play the game six times to get one win on the average. The probability 20% means that you'd have to play five times to get one win on average.
<br>For odds that are greater than one, such as 5:1, it is easy to remember that we are not dealing with probabilities because no probability can be greater than 1 (or greater than 100%), but for oods that are less than one, such as 1:5, the danger od confusion lurks around the corner.
<br>So make sure you always know when we are talking about odds when we ate talking about probabilities.
<br>The following exercises will help you practice dealing with correspondence between odds and probabilities. Don't worry if you make some mistakes at this stage: the main goal is to learn the skills that you will need in the next sections.
### exercise 09: odds
As we already mentioned above, the odds 3:1 - for example three rainy days for each rainless day - corresponfs to probability 0.75 (75% in percentages).
<br> In general, if the odds in favor of an event are x:y, the probability of the event is given by x / (x + y). Try that with the odds 3:1 if you like, You should get the answer 0.75.
<br>As we also pointed out, the odds 6:2 corresponds to exactly the same probability as the odds 3:1 because when we let x=6 and y=2, and wirte them in the formula x / (x+y), which comes out as 6/8 = 3/4 = 0.75.
<br>**Your task:**
<br>For the first three times 1-3, convert the oods to probabilies as natural frequencies; for example, from 1:1 to 1/2. Give your answer as fraction, for example 2/3.
<br>For the last three items 4-6, convert the odds into probabilities expressed as percentages (eg. 4.2 %). Give your answer in percentages using a single decimal, for example 12.2%.
<br>*Hint:* the calculations are to be calculated with a simple calculator and the formulas can be found above.

1. The odds for getting three of a kind in poker are about 1:46: 1/47.
<br>Correct. There are 46 situations where you do not get three of a kind for one where you get it, so the probability is 1/(1+46) = 1/47.
2. The odds for rain in San Diego are 23:342: 23/365
<br>Correct. There are 23 rainy days for 342 dry days, so the probability is 23/(23+342) = 23/365.
3.The odds for rain in San Diego are 23:342. 23/365
<br>Correct. There are 23 rainy days for 342 dry days, so the probability is 23/(23+342) = 23/365.
4. The odds for getting three of a kind in poker are about 1:46: 2.1%
<br>Correct. Previously we had the probability as 1/(1+ 46) = 1/47, which gives us roughly 0.0213, which rounds to 2.1%.
5. The odds for rain in Helsinki are 206:159. 56.4%
<br>Correct. Previously we had the probability as 206/(206 + 159) = 206/365, which gives us roughly 0.5644, which rounds to 56.4%.
6. The odds for rain in San Diego are 23:342. 6.3%
<br>Correct. Previously we had the probability as 23/(23 + 342) = 23/365, which gives us roughly 0.0630, which rounds to 6.3%.

## II. The Bayes rule
<h3>We will not go too far into the details of probability calculus and all the ways in which it can be used in various AI applications, but we will discuss one very important formula.</h3>
We will do this because this particular formula is both simple and elegant as well as incredibly powerful. It can be used to weigh conflicting pieces of evidence in medicine, in court of law, and in many (if not all) scientific disciplines. **The formula is called the Bayes rule (or the Bayes formula)**.
<br>We will start by demonstrating the power of the Bayes rule by mneans of a simple medical diagnosis problem where it highlights how poorly our intuition is suited for combining conflicting evidence. We will then show how the Bayes rule can be used to build AI methods that can cope with conmflicting and noisy observations.

> <h3>Prior and posterior odds</h3>
> The Bayes rule can be expressed un many forms. The simplest one is in terms of odds. The idea is to  take the odds of something happening (afainst it not happening), which we'll call prior odds. The word prior refers to our assessment of the odds before obtaining some new information that may be relevant. The purpose of the formula is to update the prior odds when new information becomes available, to obtain the posterior odds, or the odds after obtaining the information (the dictionary meaning of posterior is "something that comes after, later").
<br>![](images/7_1.svg)
### How odds change
In order to weigh the new information, and decide how the odds change when it becomes available, we need to consider how likely we would be to encounter this information in alternative situations. Let's take as an example, the odds that it will rain later today. Imagine getting up in the morning in Finland. The chances of rain are 206 in 365 (including rain, snow and hail, brrr). The number of days without rain is therefore 159. This convertis to prior odds of 265:159 for rain, so the cards are stacked against you already before you open your eyes.
<br>However, after oepning your eyes and taking a look outside, you notice it is cloudy. Suppose the chances of having a cloudy morning on a rainy day are 9 out of 10 - that means that only one out of 10 rainy days start out with blue skies. But sometimes there are also clouds without rain: the chances of having clouds on a rainless day are 1 in 10. Now how much higher arethe chances of clouds on a rainy day compared to a rainless day? Think about this carfully as it will be importantto be able to comprehend the question and obtain the answer in what follows.
<br>The answer is that the chances of clouds on a rainy day are **nine times++ as high as the chances of clouds on a rainless day: on a rainy day the chances are 9 out of 10, whereas on a rainless day the chances are 1 outof 10, which is nine times ar high.
<br>Note that even though the two probabilities 9/10 and 1/10 sum up to 9/10+1/10 = 1, this is by no means always the case. In some other town, the mornings of rainy days could be cloudy eight times out of ten. This, however, would not mean that the rainless days are cloudy two times out of ten. You'll have to be careful to get the calculations right (but never mind if you take a mistake or two - don't give up! The Bayes rule is a fundamental thinking tool for everyone of us)-
> <h3>Likelihood ratio</h3>
> The above rario (nine times hicher chances of clouds on a rainy day compared to a rainless day) is called the likelihood ratio. More generally, the likelihood ratio is the probability of the observation in case of no event (in the above, no rain), Please read the previous sentence a few times. It may look a little intimidating, but it's not possible to digest if you just focus carefully. We will walk you through the steps in detail, just don't lose your nerve. We're almost there.
So we concluded that on cloudy morning, we have: **likelihood ratio: (9/10) / (1/10) = 9**.
<br>The mighty Bayes rule for converting prior odds into posterior odds is - ta-daa! - as follows: **posterior odds = likelihood ratui * prior odds**
<br>Now you are probably thinking: Hold on, that's the formula? It's a frigging multiplication! That is the formula - we said simple, didn't we? You wouldn't imagine that a simple multiplication can be used for all kinds of incredibly useful applications, but it can. We'll study a couple of examples which will demonstrate this.
> <h3>Many forms of Bayes</h3>
> In case you have any trouble with the fillowing exercises, you may need to read the above material a few times and give ti some time, ahd if that doesn't do it, you can look for more material online. Just a woed of advice: there are many different forms in which Bayes rule can be written, and the odds form that we used isn't the most common one. There are a couple links that you may find useful:
>
> - [Math Doctor: Baye's Theoren and medical testing](https://www.youtube.com/watch?v=tRE6mKAIkno)
> - [Better explained: Understanding Bayes Theorem with ratios](https://betterexplained.com/articles/understanding-bayes-theorem-with-ratios/)

### exercise10: bayes rule (part 1of 2)
Apply the Bayes rule to calculate the **posteior offs for rain** having observed clouds in the morning in Helsinki. 
<br>As we calculated above, the prior odds for rain is **206/159** and the likelihood ratio for observing clouds is **9**.
<br>Give your results in the for of odds, xx:yy, where xx and yy are numbers (note that xx and yy does **not** mean that the numbers shouldhave two digits each). Remember that when multiplying odds, you should only mutiply the numerator (the xx part). For example, if you multiple the odds 5:3 by 5, the result is 25:3. Give the answer without simplifying the expresion even if both sides have a common factor.

1854:159 - Correct. The prior odds are 206:159. The likelihood ratio is 9, so we get the posterior odds for rain given clouds to be 9 × 206:159 = 1854:159. So in the long run, on the days when we observe clouds in the morning, we can expect 1854 rainy days for every 159 rainless days, which is about the same as 12 rainy days for one rainless day. If we wanted to express this as a probability (even though this was not the question), we could use the formula x / (x+y) to get the value 1854 / (1854+159) which is about 0.92, or about 92% chance of rain when there are clouds in the morning. Better take an umbrella.

### The Bayes rule iun practice: breast cancer screening.
Our first realistic application is a classical example using the Bayes rule, namely medical diagnosis. This example also illustrates a common bias in dealing with uncertain information called the base-rate fallacy.
<br>![](images/7_2.svg)
<br>![](images/7_3.svg)
<br>Consider mammographic sreening for breast cancer. Using made up percentages for the sake of simplifying the numbers, let's assume that 5 in 100 women have breast cancer. Suppose that if a person has breast cancer, then the mammograph test will find it 80 times out of 100. When the test comes out suggesting that breast cancer is present, we say that the result is positive, although of course there is nothing positive about this for the person being tested (a technical way of saying this is that the sensitivity of the test is 80%).
<br>The test may also fail in the other direction, namely to indicate breast cancer when none exists. This is called a false positive finding. Suppose that i f the person being tested actually doesn't have breast cancer, the chances that the test nevertheless comes out positive are 10 in 100 (In technical terms, we would say that the specifity of the test is 90%).
<br>Based on the above probabilities, you are able to calculate the likelihood ratio. You'll find use for it in the nest exercise, If you forgot how the likelihood ratio is calculated, you may wish to check the terminology box earlier in this section and revisit the rain example.
<br>Note: you can use the above diagram with sick figures to validate that your result is in the ballpark (about right) but note that diagram isn't quite precise. Out of the 95 women who don't have cancer (the gray figures in the top panel), anout nine and a half are expected to get a (false) positive result. The remaining 85 and a half are expected to get a (true) negative result. We didn't want to be so cruel as to cut people - even stick figures - in half, so we used 9 and 86 as approximation.
### exercise11: Bayes rule (part 2 of 2)
Consider the above breast cancer scenario. An average woman takes the mammograph test and gets a positive thest result suggesting breast cancer. What do you think are the oods that she has breas cancer given the observation that the test is possible?
<br>First, use your intuition without applying the Bayes rule, and write down on a piece of paper (not in the answer box below) what you think the chances of having breast cancer are after a positive test result. The intuitive answer will not be a part of your answer. It will be just for your own information.
<br>Next, **calculate the posterior odds of her having breast cancer using the Bayes rule**. This will be your answer.
<br>Hints:

1. Start by calculating the prior odds.
2. Determine the probability of the observation in case of the event (cancer).
3. Determine the probability in case if no event (no cancer).
4. Obtain the likelihood ratio as the ratio of the above two probabilities
5. Finally, multiply the prior odds by the likelihood ratio.

Enter the posterior offs as your solution below. Give the answer in the form xx:yy, where xx and yy are numbers, without simplifying the expression even if both sides have a common factor.

40:95. Correct. The prior odds describe the situation before getting the test result. Since five out of 100 women have breast cancer, there is on the average five women with breast cancer for every 95 women without breast cancer, and therefore, the prior odds are 5:95. The likelihood ratio is the probability of a positive result in case of cancer divided by the probability of a positive result in case of no cancer. With the above numbers, this is given by 80/100 divided by 10/100, which is 8. The Bayes rule now gives the posterior odds of breast cancer given the positive test result: posterior odds = 8 × 5:95 = 40:95, which is the correct answer. So despite the positive test result, the odds are actually against the person having breast cancer: among the women who are tested positive, there are on the average 40 women with breast cancer for every 95 women without breast cancer. Note: If we would like to express the chances of breast cancer given the positive test result as a probability (even though this is not what the exercise asked for), we would consider the 40 cases with cancer and the 95 cases without cancer together, and calculate what portion of the total 40 + 95 = 135 individuals have cancer. This gives the result 40 out of 135, or about 30%. This is much higher than the prevalence of breast cancer, 5 in 100, or 5%, but still the chances are that the person has no cancer. If you compare the solution to your intuitive answer, they tend to be quite different for most people. This demonstrates how poorly suited out intuition is for handling uncertain and conflicting information.

### The base rate fallacy
While doing the above exercise, youmay have noticed that our intuition is not well geared towards weighing different pieces of evidence. This is true specially when the pieces of evidence conflict with each other. In the above example, on the one hand, the *base rate* of breast cancer was relatively low, meaning that breast cancer is relatively rare. So our brain thinks that it's unlikely that a person has it. On the other hand, the positive mammograph test suggests the opposite. Our brain tends to choose one of these pieces of evidence and ignore the other. It is typically the low base rate is ignored. That's why your intuition probably says that the psoterior probability of having breast cancer given the psoitive test result is much higher than 30%. This is known as the so called [base rate fallacy](https://en.wikipedia.org/wiki/Base_rate_fallacy). Knowing the Bayes rule is the best cure against it.

## III. Naive bayes classification
<h3>One of the most useful applications of the Bayes rule is the so-called naive Bayes classifier.</h3>

The Bayes classifier is a machine learning technique that can be used to classify objects such as text documents into two or more classes. The classifier is trained by analyzing a set of training data, for which the correct classes are given.
<br>The naive Bayes classifier can be used to determine the probabilities of the classes given a number of different observations. THe assumption in the model is that the feature variables are conditionally independent given the class (we will not discuss the meaning of conditional independece in this course. For our purposes, it is enough to be able to exploit conditional indepence in building the classifier).

### Real world application: spam filter
We will use a spam email filter as a running example for illustrating the idea of the naive Bayes classifier. Thus, the class varaible indicates whether a messge is spam (or "junk email") or whether it is a legitimate message (also called "ham"). The words in the message correspond to the feature variables, so that the number of feature variables in the model is determined by the length of the message.
><h3>Why we call it "naive"</h3>
>Using spam filters as an example, the idea is to think of the words as being produced by shoosing one word after the other so that the choice of the word depends only on whether the message is spam ir ham. This is a crude simplification of the process because it means that tthere is no dependency between words, and the order of the words has no significance. This is in fact why the method is called naive,

Because the model is based on the idea that the words can be processed independently, we can identify specific words that are indicative of either spam ("FREE", "LAST") or ham ("meeting", "algorithm").
<br>![](images/8_1.svg)
<br>Despite its naivete, the naive bayes method tends to work very well in practice. This is a good example of the common saying in statistics, "all models are wrong, but some are useful" means (the aphorism is generally attributed to statiscian [George E. P. Box](https://en.wikipedia.org/wiki/George_E._P._Box))

### Estimating parameters
To get started, we need to specify the prior to specify the prior odds for spam (against ham). For simplicity assume this to be 1:1 which means that on the average of the incoming messages are spam (in reality, the amount of spam is probably much higher).
<br>To get our likelihood ratios, we need two different probabilities for any word occurring: one in spam messages and another one in ham messages.
<br>The word distributions for the two classes are best estimated from actual training data that contains some spam messages as well as legitimate messages. The simplest way is to count how many times each word, abacus, acacia, ..., zurg, appears in the sata and divide the number by the total word count.
<br>To illustrate the idea, let's assume that we have at our disposal some spam and some ham. You can easyly obtain such data by saving batch of your emails in two files.
<br>Assume that we have calculated the number of occurrences of the following words (along with all other words) in the two classes of messages. 

| **word** 	| **spam** 	| **ham** 	|
|---	|---	|---	|
| million 	| 156 	| 98 	|
| dollars 	| 29 	| 119 	|
| adclick 	| 51 	| 0 	|
| conferences 	| 0 	| 12 	|
| **total** 	| 95791 	| 306438 	|

We can now estimate that teh probability taht a word in a spam message is a "million", for example, is about 156 out of 95791, which is roughly the same as 1 in 614. Likewise, we get the estimate that 98 out of 306438 words, which is about the same as 1 in 3127, in a ham message are million. Noth of these probability estimates are small, less than 1 in 500, but more importantly, the former is higher than the latter: 1 in 614 is higher than 1 in 3127. This means that the likelihood ratio, which is the first ratio divided by the second ratio, is more than one. To be more precise, the ratio is (1 / 614) / ( 1 / 3127) = 3127 / 614 = 5.1 (rounded to one decimal digit).
<br>Recall that if you have any trouble at all with following the math in this section, you should refresh the arithmetic with fractions using the pointers we gave earlier (see the part about Odds in section *Odds and Probability*).
><h3>Zero means trouble</h3>
>One problem with estimating the probabilities directly from the counts is that zero counts lead to zero estimates. This can be quite harmful for the performance of the classifier - it easily leads to situations where the posterior odds are 0/0, which is nonsense. The simplest solution is to use a small lower bound for all probability estimates. The value 1/100000, for instance, does the job.

Using the above logic, we can determine the likelihood ratio for all possible words without having to use zero, giving us the following likelihood ratios:

| **word** 	| **likelihood ratio** 	|
|---	|---	|
| million 	| 5.1 	|
| dollars 	| 0.8 	|
| adclick 	| 53.2 	|
| conferences 	| 0.3 	|

We are now ready to applu the method to classify new messages.

### Example is it spam or ham?
Once we have the prior odds and the likelihood ratios calculated, we are ready to apply the Bayes rule, which we already practiced in the medical daignosis case as our example. The reasoning goes just like it did before: we updated the odds of spam by multiplying it by the likelihood ratio. To remind ourselves of the procedure, let's try a message with a single word to begin with. For the prior odds, as agreed above, you whould use odds 1:1.
### exercise12: one word spam filter.
Let's start with a message that only has one word in it: "million".
<br>**Your task**: Calculate the **posterior odds** for spam given this word using the table above, starting from prior odds 1:1. Keep in mind that the odds is **not** the same as the probability, which we would usually express as a percentage.
<br>**Give your answer in the form od a single decimal number x.x using the dot '.' as the decima separator.**
<br>(Remember that odds can be represented as xx:yy or simply as a single decimal number, say z.z (where z.z = xx/yy). You may wish to revisit the discussion on this just before [exercise 09](#exercise-09-odds)).

5.1. Correct. As you may have noticed, the structure of this exercise is identical to that of the previous exercise about medical diagnosis. We have the class label spam or ham, and one piece of evidence that we can use to update our prior odds to obtain the posterior odds. We decided above that the prior odds are 1:1. The likelihood ratio is obtained by dividing the probability of the word 'million' in spam divided by the probability of the word 'million' in ham. This we already calculated above, and it can be found in the table of likelihood ratios: the value is 5.1. Now multiply the prior odds by the likelihood ratio to get 1:1 × 5.1 = 5.1. This is the posterior odds. Again, the posterior odds means that for messages that include the word 'million', there are on the average 5.1 spam messages for every ham message. Or to use whole numbers, there are 51 spam messages for every 10 ham messages. The probability value is therefore 51 / (51+10) = 51/61, or approximately 83.6 %.

To handle the rest of the words in a message, we can use exactly the same procedure. The prosterior odds after one word, which you calculated in the previous exercise, will become the prior for the next word, and so on.

### exercise13: full spam filter
Now use the naive Bayes method to calculate the posterior odds for spam given the message "million dollars adclick conferences".
<br>You should again start with the prior odds 1:1, and then multiply the odds repeatedly by the likelihood ratios for each of the four words. Notice taht the likelihood ratios are tabulated above for your reference (these are the numbers 5.1, 0.8, and so on).
<br>**Your task**: Express the result as psoterior odds without any rounding of the result. You may take a look at the solution of the previous exercise for help.

65.1168: Correct. We start in the same way as the previous exercise. Multiplying the prior odds by the likelihood ratio 5.1 (for the word 'million') gives posterior odds 5.1. Next we'll simply keep multiplying the odds by the likelihood ratios for the rest of the message. The likelihood ratios can be found in the table above: 0.8 ('dollars'), 53.2 ('adclick'), and 0.3 ('conference'). The product of all these numbers equals 1:1 × 5.1 × 0.8 × 53.2 × 0.3 = 65.1168. This means that for messages that include all these four words, there are on the average about 65 spam messages for each ham message, or about 651 spam messages for every 10 ham messages. If we wanted to get the probability value (which was not asked), it is about 651 / (651+10) = 651 / 661 or approximately 98.5 %. This message would probably end up in your junk mail folder.

Hooray! You have now mastered a powerful technique used every day in a wide range of real-world AI applications, the naive Bayes classifier. Even if you had to skip some of the technicalities, you should try to make sure you understood the basic principles of applying probabilities to update beliefs. As we discussed in the beginning of this chapterm the main advantage of probabilistic reasoning is the ability to handle uncertain and conflicting evidence. Using examples in medical diagnosis and spam filtering, we demonstrated how this works in practice.
## Recap
<h3>After completing chapter03 you should be able to:</h3>

- Express probabilities in terms of natural requencies
- Apply the Bayes rule to infer in simple scenarios
- Explain the base-rate fallacy and avoid it by applying Bayesian reasoning.

# Chapter 04: Machine Learning

<h3>It has been long understtod that learningis a key element of intelligence. This holds both for natural intelligence - we all get smarter by learning - and artificial intelligence.</h3>

## I. The types of machine learning
<h3>Handwritten digits are a classic case that is often used when discussing why we use machine learning, and we will make no expception.</h3>
Below you can see examples of handwritten images from the very commonly used MNIST dataset:

![](images/9_1.svg)
<br>The correct label (what digit the writer was supposed to write) is shown above each image. Note that some of the "correct" class labels are questionable: see for example the second image from the left: is that really a 7 or actualli a 4?

><h3>MNIST - what's that?</h3>
>Every machine learning student knows about the MNIST dataset. Fwewer know what the acronym stands for. In dact, we had to look it up to be able to tell you that the M stands for `Modified`, and NIST stands for `National Institute of Standards and Technology`. Now you know something that an average machine learning expert doesn't!
In the most common machine learning problems, exactly one class value is correct at a time. This is also true in the MNIST case, although as we said, the correct answer may often be hard to tell. In this kind of problem, it is possible that an instance belongs to multiple classes (or none at all) at the same time. What we would like to achieve is an AI method that can give an image like the ones above, and automatically spits out the correct label.
><h3>How to solve the problem</h3>
>An automatic digit recognizer could in principle be built manually by writing down rules such as:
> 
>- if the black pixels are mostly in the form of a single loop, then the label is 0.
>- if the pixels form two intersecting loops then the label is 8.
>- if the black pizels are mostly in a straight vertical line in the middle of the figure then the label is 1.
><br>and so on...
>
>This is how AI methods were mostly developed in the 1980s (so called "expert systems"). However, even for such a simple task as digit recognition, the task of writing such rules is very laborious. In fact the above example rules wouldn't be specific enouth to be implemented by programming - we'd have to define precisely what we mean by "mostly", "loop", "line", "middle", and so on.
><br>And even if we did all this work, the result would likely be a bad AI mehtod because as you can see, the handwritten digits are often a bit so-and-so, and every rule would need a dozen exceptions.
### Three types of machine learning
The roots of machine learning are in statistics, which can also be thought as the art of **extracting knowledge from data**. Expecially methods such as linear regression and Bayesian statistics, which are both already more than two centuries old, are even today the heart of machine learning. For more examples and a brief history, see the [timeline of machine learning](https://en.wikipedia.org/wiki/Timeline_of_machine_learning) (Wikipedia).
<br>The area of machine learning is often divided in subareas accordning to the kinds of problems being attacked. A rough categorizations is as follows:
<br>**Supervised learning:** We are given an input, for example a photograph woth a traffic sign, and the task is to predict the correct output or label, for example whcih traffic sign is the picture (speed limit, stop signt, etc.). In the simplest cases the answers are in form of yes/no (we call these *binary classification problems*).
<br>**Unsupervised learning:** There are no labels or correct outputs. The task is to dicover the structure of the data: for example, grouping similar items to form "clusters", or reducing the data to a small number of important "dimensions". Data visualization can also be considered unsupervised learning.
<br>**Reinforcement learning:** Commonly used in situations where an AI agent like a self-driving car must operate in an environment and where feedback about good or bad choices is available with some delay. Also used in games where the outcome may be decided only at the end of the game.
<br>The categories are somewhat overlapping and fuzzy, so particular method can sometimes be hard to place in one category. For example, as the name suggests, so-called **semisupervised learning** is partly supervised and partly unsupervised.

><h3>Classification</h3>
>When it comes to machine learning, we will focus primarly on supervised learning, and in particular, classification tasks. In classification, we observe an input, such as a photograph of a traffic sign, and try to infer its "class", such as the type of sign (speed limit 80 km/h, pedestrian crossing, stop sign, etc.). Other examples of classification tasks include: identification of fake twitter accounts (input includes the list of followers, and the rate at which they have started following the account, and the class is either fake or real account) and handwritten digit regodnition (input is an image, class is 0, ..., 9).
<br>![](images/9_2.svg)
### Humans teaching machines: supervised learning
Instead of manually writing down exact rules to do the classification, the point in supervised learning is to take a number of examples, label each one by the correct label, and use them to "train" an AI method to automatizally recognize the correct label for the training examples as well as (at least hopefully) any other images. This is of course requires that the correct labels are provided, which is why we talk about supervised learning. The user who provides the correct ,labels is a supervisor who guides the learning algorithm towards correct answers so that eventually, the algorithm can independently produce them.
<br>In addition to learning how to predict the correct label in a classification problem, supervised learning can also be used in situations where the predicted outcome is a number. Examples include predicting the number of people who will cleick a Google ad based on the ad content and data about the user's prior online behavior, predicting the number of traffic accidents based on road conditions and speed limit, or predicting the selling price of real estate based on its location, size and condition- These problems are called *regression*. You probably recognize the term *linear regression*, which is a classicalm still very popular technique for regression.
><h3>Example</h3>
>Suppose we have a data set consisting of apartment sales data. For each purchase, we would obviously have the price that was paid, together with the size of the apartment in square meters (or square feet, if you like), and the number of bedrooms, the year of construction, the condition (on a scale from "disaster" to "spick and span"). We could then use machine learning to train a regression model that predicts the selling price based on these features. See a [real-life example here](http://kannattaakokauppa.fi/#/en/).
<br>![](images/9_3.svg)
### Caveat: careful with that machine learning algorithm
There are a acouple of potential mistakes that we'd like to make you aware of. They are related to the fact that unless you are careful with the way you apply machine learning methods, you could become too confident about the accuracy turns out to be worse than expected.
<br>The first thing to keep in mind in order to avoid big mistakes, is to split your data set into two parts: the **training data** and the **test data**. We first train the algorithm using only the training data. This cives us a model or a rule that predicts the output based on the input variables.
<br>To asses how well we can actually predict the outputs, we can't count on the training data. While a model may mbe a very good predictor in the training data, it is no proof that it can **generalize** to any otehr data. THis is where the test data comes in handy: we can apply the trained model to predict the outputs for the test data and compare the predictions to the actual outputs (for example, future apartment sale prices).
><h3>Too fit to be true! Overfitting alert</h3>
>
>It is very important to keep in mind that the accuracy of a predictor learned by machine learning can be quite different in the training data and in seperate test data. This is the so-called **over-fitting** phenomenon, and a lot of machine learning research is focused on avoding in one way or another. Intuitively, overfitting means trying to be too smart. When predicting the success of a new songs, and come up with a rule like "if the song is about love, and includes a catchy chorus, it will be top-20". However, maybe there are two love songs with catchy choruses that didn't make the top-20, so you decide to continue the rule "... except if Sweden or yoga are mentioned" to improve your rule. This could make your rule fit past data perfectly, but it could in fact make it work **worse on future test data**.
>Machine learning methods are especially prone to overfitting because they can try a huge number of different "rules" until one that fits the training data perfectly is found. Especially methods that are very flexible and can adapt to almost any pattern in the data can overfit unless the amount of data is enormous. For example, compared to quite restricted linear models obtained by linear regression, neural networks can require massive amounts of data before they produce reliable prediction.

Learning to avoid overfitting and choose a model that is not too restricted, nor too flexible, is one of the most essential skills of a data scientist.

### Learning without a teacher: unsupervised learning
Above we discussed supervised learning where the correct answers are available, and the task of the machine algorithm is to find a model that predicts them based on the input data.
<br>In supervised learning, the correct answers are not provided. This makes the situation quite different since we can't build the model by making it fit the correct answers on training data. It also makes the evaluation of performance more complicated since we can't check whether the learned model is doing well or not.
<br>Typycal unsupervised learning methods attempt to learn some kind of "structure" underlaying the data. This can mean, for example, **visualization** where similar items are placed near each otehr and dissimilar items further away from each other. It can also mean **clustering**, where we use the data to identify groups or "clusters" of items that are similar to each other but dissimilar from data in other clusters.
><h3>Example</h3>
>As a complete example, grocery store chains collect data about their customers' shopping behavior (that's why you have all those loyalty cards). To better undrstand their customers, the store can either visualize the data using a graph where each customer is represented by a dot and customers who tend to by the same products are placed nearer each other than customers who buy different products. Or, the store could apply clustering to obtain a det of customer groups such as 'low-budget health food enthusiasts', 'high-end fish lovers', 'soda and pizza 6 days a week', and so on. Note that a machine learning method would only group the customers into clusters, but it wouldn't automatically generate the cluster labels ('fish lovers' and so on). This task would be left for the user.

Yet another example of unsupervied learning can be termed **generative modeling**. This has become a prominent approach over the last few years as a deep learning technique called generative adversarial networks (GANs) has lead to great advances. Given some data, for example, photographs of people's faces, a generative model can generate more of the same: more real-looking but artificial images of people's faces.
<br>We will return to GANs and the implications of being able to produce high-quality artifical image content a bit later in the course, but next we will take a closer look at supervised learning and discuss some specific methods in more detail.

## II. The nearest neighbor classifier

<h3>The nearest neighbor classifier is among the simplest possible classifiers. When given an item to classify, it finds the training data item that is most similar to the new item, and outputs its label. An example given is the folowing diagram.</h3>

![](images/10_1.svg)

In the above diagram, we show a collection of training data items, some of which belong to one class (green) and other to another class (blue). In addition, there are two test data items, the stars, which we are going to classify using the nearest neighbor method. 
<br>The two test items are both classified in the "green" class because their nearest neighbors are both "green" class because their nearest neighbors are both green (see diagram (b) above).
<br>The possition of the points in the plot represents in some way the properties of the items. Since we draw the diagram on a flat two-dimensional surface - you can move in two independent directions: up-down and left-right - the items have two properties that we use for comparison. Imagine for example representing patients at a clinic in terms of their age and blood-sugar level. but the above diagram should be taken just as a visual  tool to illustrate the general idea, which is to relate the class values to similarity or proximity (nearness). THe general idea is by no means restricted into two dimensions and the nearest neighbor classifier can easily applied to items that are characterized by many more properties than two.

### What do we mean by nearest?

An interesting questin related (among other things) the nearest neighbor classifier is the definition of distance or similarity between instances. In the illustration above, we tacitly assumed that the standard geometric distance, technically called the Euclidean distance, is used. This simply means taht if the points are drawn on a piece of paper (or displayed on your screen), you can measure the distance between any two items by pulling a piece of thread straight from one to the other and measuring the length.
> <h3>Defining nearest</h3>
>Using the geometric distance to decide which is the nearest item may not always be reasonable or even possible: the type of the input may, for example, be text, where it is not clear how the items are drawn in a geometric representation and how distances should be measured. You should therefore shoose the distance metric on a case-by-base basis.
In the MNISt digit recoginition case, one common way to measure image similarity, is to count pixel-by-pixel matches. In other words, we compare the pixels in the top-left corner of each image to one another and if the more similar color (shade of gray) they are, the more similar the two images are. We also compare the pixels in the bottom-right corner of each image, and all pixels inbetween. This technique is quite sensitive to shoifting or scaling the images: if we take an image of a "1" and shof it ever so slightly either left or right, the outcome is that the two images (before and after the shift) are very different because the black pixels are in different positions in the two images. Fortunately, the MNIST data hs been preprocessed by centering the images so that the problem is alleviated.

![](images/10_2.svg)

### Using nearest neighbors to predict user behavior
A typical example of an application of the nearest neighbor algorithm is predicting user behavior in AI applications such as recommendation systems.
<br>The idea is to use the very simple principle that users with similar past behavior tend to have a similar future behavior. Imagine a music recommendation system that collects data about users' listening behavior. Let's say you have listened to 1980s disco music (just for the sale of argument). One day, the servide provider gets their hands on a hard-to-find 1980 disco classic, and adds it to the music library. The system now needs to predict whether you will like it or not. One way of doing this is to use information about the genre, the artist, and other metadata, enetered by the good people of the service provider. However, this information is relatively scarce and coarse and it will only be available to give rough predictions.
<br>What current recommendation systems use instead of the manually entered metadata, is something called collaborative filtering. The collaborative aspect of it is that is used other users' data to predict your preferences. The word "filter" refers to the fact that you will be only recommended content that passes through a filter: content that you are likely to enjoy will pass, other content will not (these kinds if filters may lead to the so called filter bubbles, which we mentioned in Chapter 1. We will return to them later).
<br>Now let's say that other users who have listened to 80s music enjoy the new release and keep listening to it again and again. THe system will identify the similar past behavior that you and other 80s disco fanatics share, and since other users like you enjoy the release, the system will predict that you will too. Hence it will show up at the top of your recommendation list. In an alternative reality, maybe the added song is not so great and other users with similar past behavior as yours don't really likeit. In that case, the sustem wouldn't botherrecommending it to you or at lesast it wouldn't be at the top of the list of recommendations for you.
<br>The following exercises will illustrate this idea.
### exercise 14: customers who bought similar products
In this exercise, we will build a simple recommendation system for an onlime shopping application where the users' purchase history is recorded and used to predict which products is likely to buy next.
<br>We have data from six users. For each user, we have recorded their recent shopping history of four items and the item they bought after buying these four items:

| User | Shopping history |  |  |  | Purchase |
|---|---|---|---|---|---|
| Sanni | boxing gloves | Mody Dick (novel) | headphones | sunglasses | coffee beans |
| Jouni | t-shirt | coffe beans | coffee maker | coffee beans | coffee beans |
| Janina | sunglasses | sneakers | t-shirt | sneakers | ragg wool socks |
| Henrik | 2001: A Space odyssey (dvd) | headphones | t-shirt | boxing gloves | flip flops |
| Ville | t-shirt | flip flops | sunglasses | Moby Dick (novel) | sunscreen |
| Teemu | Moby Dick (novel) | coffee beans | 2001: A SpaceOdyssey (dvd) | headphones | coffee beans |

The most recent purchase is the one in the rightmost column, so for example, after buying a t-shirt, flip flops, sunglasses, and Moby Dick (novel), Ville bought sunscreen. Our hypothesis is that after buying similar items, other users are also likely to buy sunscreen.
<br>To apply the nearest neighbor method, we need to define what we mean by nearest. This can be done in many different ways, some of which work better than others. Let's use the shopping history to define the similarity ("nearness") by counting how many of the items have been purchased by both users.
<br>For example, users Ville and Hwendrik have both bought a t-shirt, so their similarity is 1. Note that flip flops doesn't count because we don't include the most recent purchase when calculating the similarity -- it is reserved for another purpose.
<br>Our task is to predict the next purchase of customer Travis who has bought the following products:

| User | Shopping History |  |  |  | Purchase |
|---|---|---|---|---|---|
| Travis | green tea | t-shirt | sunglasses | flip flops | ? |

You can think of Travis being our test data, and the above six users make our training data.
<br>**Proceed as follows:**
<br>1. Calculate the similarity of Travis relative to the six users in the training data (done by adding together the number of similar purchases by the users).
<br>2. Having calculated the similarities, identify the users who is most similar to Travis by selecting the largest of the calculated similarities.
<br>3. Predict what Travis is likely to purchase next by looking at the most recent purchase (the rightmost column in the table) of the most similar form the previous step.
<br>Who is the most similar to Travis? Ville
<br>What is the predicted purchase for Travis? Sunscreen
![](images/10_3.svg)
<br>In the above example, we only had six users' data and our was probably very unreliable. However, online shopping sites often have millions of users, and the amount if data they produce is massive. In many cases, there are a horde of users whose past behavior is very similar to yours, and whose purchase history gives a pretty good indication of your interests.
<br>These predictions can also be self-fulfilling prophecies in the sense that you are more likely to buy a product if it is recommended to you by the system, which makes it tricky to evaluate how well they actually work. The same kind of recommendation systems are also used to recommend music, movies, news, and social media content to users. In the context of news and social media, filters created by such systems can lead to filter bublles.
### exercise 15: filter bubbles
A discussed above, recommending news or social media content that a user is likely to click or like, may lead to filter bubbles where the users only see content that is in line with their own values and views.
1. Do you think that filter bubbles are hamful? After all, they are created by recommending content that the user likes. What negative consequences, if any, may be associated with filter bubbles? Feel free to look for more information from other sources.
2. Think of ways to avoid filter bublles while still being able to recommend content to suit personal preferences. Come up with at least one suggestion. You can look for ideas from other sources, but we'd like to hear your own ideas too!
**Note:** your answer should be at least a few sentences for each part.
**Note:** On using ChatGPT and similar models: We appreciate you putting an AI tool into use. Feel free to consult it but note that since we are interested in your own opinion, we expect you to write your final answers yourself.

Answer: Filter bubbles may be harmful because they create an echo chamber effect. On social media, you are no longer exposed to content that opposes your profile because social media analyzes your behavior patterns and displays information that they believe is relevant to you based on your online behavior. This creates a bubble of similar users and suggests things that they have also checked, thereby limiting your exposure to different opinions or beliefs and reinforcing your existing viewpoint.
In addition to the filter bubble, social media exposes users to extremely polarizing content, as it tends to generate the most impact on viewers and can potentially radicalize them. This creates a loop that contributes to a more closed-minded and narrow society.
The most efficient way to avoid being affected by the filter bubble is by not accepting cookies and clearing your browser history, or browsing in incognito mode. This ensures that there is no trace of your profile on the internet and prevents it from contributing to the filter bubble.
Another way to counteract this phenomenon, while still benefiting from algorithmic influence, is to "escape" the algorithm. This involves actively seeking out social media profiles that present opposing viewpoints to what you already believe. By exposing yourself to diverse perspectives, you can reeducate the algorithm and receive recommendations that encompass a wider range of views.
Additionally, it is important to develop critical thinking skills and evaluate the filtered information you receive. Consider whether it represents the actual reality or if it is a partial point of view. By questioning and analyzing the information, you can gain a more comprehensive understanding of various topics and avoid being solely influenced by the filter bubble effect.

## III. Regression
<h3>Our main learning objective in this section is another nice example of supervised learning methods, and almost as simple as the nearest neighbor classifier too: linear regression. We'll introduce its close cousin, logistic regression as well.</h3>

> <h3>The difference between classification and regression</h3>
>There is a small but important difference in the kind of predictions that we should produce in different scnarios. WHile for example the nearest neighbor classifier chooses a class label for any item out of a given set of alternatives (like spam/ham, or 0,1,2,...,9), linear regression produces a numerical prediction that is not constrained to be an integer (a whole number as supposed to something like 3.14). So linear regression is better suited in situations where the output variable can be any number like the price of a product, the distance to an obstacle, the box-office revenue of the next Star Wars movie, and so on.

The basic idea in linear regression is to add up the effects of each of the feature variables to produce the predicted value. The technical term for the adding up process is _linear combination_. The idea is very straightforward, and it can be illustrated by your shopping bill.

><h3>Thinking of linear regression as a shopping bill</h3>
>Suppose you go to the grocery store and buy 2.5 kg of tomatoes, 1.0 kg of carrots, and two bottles of milk. If the price of potatoes is 2€/kg, the price of carrots is 4€/kg and a bottle of milk costs 3€, then the bill, calculated by the cashier, totals 2.5*2€ + 1.0*4€ + 2*3€ = 15€. In linear regression, the amount of potatoes, carrots, and milk are inputs in the data. THe output is the cost of your shopping, which clearly depends on both price and how much of each product you buy.

The word linear means that the increase in the output when one input feature is increased by some fixed amount is always the same. In other words, wheneve ryou add, say, two kilos of carrots into your  shopping basket, the bill goes up 8€. When you add another two kilos, the bill goes up another 8€, and if you add half as much, 1kg, the bill goes up exactly half as much, 4€.

><h3>Coefficients or weights</h3>
>In linear regression terminology, the prices od the different products would be called coefficients or weights (this may appear confusing since we measured the amount of potatoes and carrots by weight, but do not let yourself be tricked by this). One of the main advantages of linear regression is that is its easy interpretability: the learned wights may in fact be more interesting than the predicted outputs.

>For example, when we use linear regression to predict the life expectancy, the weight of smoking (cigarettes per day) is about minus half a year, meaning that smoking one cigarette per day takes you on the average half a year closer to termination. Likewise, the weight of vegetable consumption (handful of vegetables per day) has wight plus one yeear, so eating a handful of greens evey day gives you on the average one more year.

### exercise016: linear regression
Suppose that an extensive study is carried out, and it is found that in a particular country, the life expectancy (the average number of years that people live) among non-smoking women who don't eat any vegetables is 80 years. Suppose further that on the average, men live 5 years less. Also take the numbers mentioned above: every cigarette per day reduces the life expectancy by half a year, and a handful of veggies per day increases it by one year.

Calculate the life expectancies for the following example cases:

For example, the first case is a male (subtract 5 years), smokes 8 cigarettes per day (subtract 8 * 0.5 = 4 years), and eats two handfuls of veggies per day (add 2 * 1 = 2 years), so the predicted life expectancy is 80 - 5 - 4 + 2 = 72 years.

|Gender |	Smoking (cigarettes per day)	|Vegetables (handfuls per day)	| Life expectancy (years) |
| -- | -- | -- | -- |
| male | 8 |	2 |	73 |
| male | 0 |	6 |	A |
| female |	16 | 	1 |	B |
| female |	0 |	4 |	C |

**Your task**: Enter the correct value as an integer (whole number) for the missing sections A, B, and C above.

A - 81: Correct. A: 80 - 5 + 6 = 81

B - 73: Correct. 80 - 8 + 1 = 73

C - 84: Correct. 80 + 4 = 84

In the above exrecise, the life expectancy of non-smoking, veggie-hating women, 80 years, was the starting point for the calculation. The technical term for the starting point is the **intercept**. We will return to this below when we discuss how to learn linear regression models from data.

### Learning linear regression

Above, we discussed how predictions areobtained from linear regression when both the weights and the input features are known. So we aregiven the inputs and the weight, and we can produce the predicted output.

When we are given the inputs and the outputs for a number of items, we can find the weights such as the predicted output matches the actual output as well as possible. This is the task solved by machine learning.

> <h3>Example</h3>
>Continuing the shopping analogy, suppose we were given of a number of shopping baskets and the total bill for each of them, and we were asked to figure out the price of each of the products (potatoes, carrots, and so on). From one basket, say 1kg of sirloin steak, 2kg of carrots, and a bottle of CHianti, even if we knew that the total bill is 35€, we couldn't determine the prices because there are many sets of prices that will yield the same total bill. With many baskets, however, we will usually be able to solve the problem.

But the problem is made harder byt the fact that in the real world, the actual output isn't always fully determined by the input, becasue of varius factors that introduce uncertainty or "noise" into the process. You can think of shopping at a bazaar where the prices for any given product may vary from time to time, or a restaurant where the final damage includes a variable amount of tip. In such situations, we can estimate the prices but only with some limited accuracy.

Finding the weights that optimize the match between the predicted and the actual outputs in the training data is a classical statistical problem dating back to the 1800s, and it can be easily even for massive data sets.

We will not go into the details of the actual weight-fining algorithms, such as the classical least squares technique, simple as they are. However, you can get a fell of finding trends in data in the following exercises.

### Visualizing linear regression

A good way to get a fell for what linear regression can tell us is to draw a chart containing our data and our regression results. As a simple toy example our data set has one variable, the number of cups of coffee and employee drinks per dar, and the number of lines of code written er day by that employee as the output. This is not a real data set as obviously there are other factors having an effect on the productivity of an employee other than coffee that interact in complex ways. The increase in productivity by increasing the amount of coffee will also hold only to a certain point after it jitters distract too much.

![](images/10_4.PNG)

When we preesent our data in the chart above as points where one point presents one employee, we can see that there is obviouslyu a trend that drinking more coffee results in more lines of code being written (recall taht this is completely made-up data). From this data set we can learn the coefficient, or the weight, related to coffee consumption, and by eye we can already say that it seems to be somewhere close to five, since for each cup of coffee consumed the number oflines programmed seems to go up roughly by five. For example, employees who drink around two cups of coffee per day seem to produce around 20 lines ofcode per day, and similarly at four cups of coffee, the amount of lines produce is around 30.

It can also be noted that employees who do not drink coffee at all also produce code, and is hown by the graph to be about ten lines. This number is the intercept term that we mentioned earlier. The intercept is another parameter in the model just like the weights are, that can be learned from the data. Just as in the life expectancy example it can be thought od as the starting point of our calculations before we have added in the effects of the input variable, or variables if we have more than one, be it coffee cups in this example, or cigarettes and vegetables in the previous one.

The line in the chart represents our predicted outcome, where we have estimated the intercept and the coefficient by using an actual liner regression technique called least squares. This line can be used to predict the number of lines produced when the input is the number of cups of coffee. Note that we can obtain a prediction even if we allor only partial cups (like half, 1/4 cups, and so on).

### exercise 17: life expectancy and education (part 1 of 2)
Let's study the link between the total number of years spent in school (including everything between preschool and university) and like expectancy. Here is data from three different countries displayed in a figure represented by dots:

![](images/10_5.jpeg) 

We have once country where the average number of years in school is 10 and life expectancy is 57 years, another country where the average number of years in school is 13 and life expectancy is 53 years, and a third country where the average number of years in school is 20 and life expectancy is 80 years.

You can drag the end points of the solid line to position the line in such way that it follows the trend of the data points. Note that you will not be able to get the line fit perfectly with the data points, and this is fine: some of the data points will lie above the line, and some below it. The most important part is that the line describes the overall trend.

After you have positioned the line you can use it to predict the life expectancy.

Given the data, what can you tell about the life expectancy of people who have 15 years of education? Important: Notice that even if you can obtain a specific prediction, down to a fraction of a year, by adjusting the line, you may not necessarily be able to give a confident prediction. Take the limited amount of data into account when giving your answer.

It is probably less than 90 - Correct. The few data points that we have make it impossible say almost anything about the life expectancy only based on the data. Of course, one can know a great deal about life expectancy from other sources but the data in the above chart is insufficient to do so. The first choice is clearly stating too much. While the intervals in the second and the third choice are likely to be valid, the word 'certainly' makes them unjustified. There is a chance, greater than zero, that the value turns out to be, for example, greater than 70. Thus the only choice that we can be comfortable with is the fourth one.

### exercise 18: life expectancy and education (part 2 of 2)

In the previous exercise, we only had data from three countries. The full data set consists of data from 14 different countries, presented here in a graph:

![](images/10_6.jpeg)

Based on this data, would your prediction about the life expectancy of people with 15 years of education change? If so, why?

Which of the following options would bes match your estimate of the life expectancy for people with 15 years of education? Choose the most specific option that you think is justified by fitting the straight line model to the above data.

Probably between 50 and 90 years - Correct: The first choice would clearly be an odd estimate since the data strongly suggest that very few countries have life expectancy less than 50, and none of the data points with more than 12 years of education fall below 50. We can't be sure, of course, but life expectancy between 45 and 50 years would in this case be highly unexpected. The second choice is correct because it fits the general trend, and all data points with more than 12 years of education fall within this interval. The interval 69 to 71 years in the third choice could well include the actual value, but based on the above data, it would be too bold to claim to know the outcome with such high accuracy. The interval 15 to 150 years of the fourth choice would almost certainly include the actual value, but we think that it would be a poor summary of what we can learn from the data for the reason that it is too vague.

It should be pointed oyt that studies like those used in the above exercises cannot identify causal relationships. In other ords, from this data alone, it is impossible to say whether studying actually increases life expectancy through a better-informed and healthier life-style or other mechanisms, or whether the apparent association between life expectancy and education is due to underlying factors that affects both. It is likely that, for example, in countries where people tend to be highly educated, nutrition, healthcare, and safety are also better, which increases life expectancy. With this kind of simple analysis, we can only identify associations, which can nevertheless be useful for prediction.

### Machine learning applications of linear regression

Linear reegression is truly the workhorse of many AI and data science applications. It has its limits but they are often compensated by its simplicity, interpretability and efficiency. Linear regression has been succesfully used in the following problems to give a few examples:

- prediction of click rates in online advertising.
- prediction of retail demand for products
- predicion of box-pffice revenue of Hollywood movies
- prediction of software cost
- prediction of insurance cost
- prediction of crimes rates
- prediction of real estate prices

### Could we use regression to predict labels?

As we discussed above, linear regression and the neares neighbot method produce different kinds of predictions. Linear regression outputs numerical outputs while the nearest neighbor method produces labels from a fixed set of alternatives ("classes").

Where linear regression excels compared to nearest neighbors is interpretability. What do we mean by this? You could say that in a way, the nearest neighbor method and any single prediction that it produces are easy to interpret: it's just the nearest training data element! This is true, but when it comes to the interpretability of the learned model, there is a clear difference. Interpreting the trained model in the nearest neighbors in a similar fashion as the weights in linear regression is impossible: the learned model is basically the whole data, and it is usually way too big and complex to provide us with much insight. So what if we'd like to have a method that produces the same kind of outputs as the nearest neighbor, labels, but is interpretable like linear regression?

### Logistic regression to the rescue!

Whell there is good news for you: wwe can turn the linear regression method's outputs into predictions about labels. The technique for doing this is called logistic regression. We will not go into the technicalities, suffice to say that in the simplest case, we take the output from linear regression, ehich is a number, and predict one label A if the output is greater than sqro, and another label B if the output is less than or equal to zero. Actually, instead og just predicting one class or another, logistic regression can also give us a measure of uncertainty of the prediction. So if we are predicting whether a customer will buy a new smartphone this year, we can get a prediction that customer A will buy a phoine with probability 90%, but for another, less predictable customer, we can get a prediction that will *not* buy a phone with 55% probability (or in other words, that they will buy a pphone with 45% probability).

It is also possible to use the same trick to obtain predictions over more than two possible labels, so instead of always predicting either yes or now (buy a new phone or not, fake news or real news, and so forth), we can use logistic regression to identify, for example,m handwritten digits, in ehich case there are ten possible labels.

<h4>An example of logistic regression</h4>

Let's suppose that we collect data of students taking an introductionary couse in cookery. In addition to the basic information such as the strudent ID, name, and so on, we also ask the students to report how many hours they studied for the exam (however you study for a cookery exam, probably cooking?) - and hope that they are more or less honest in their reports. After the exam, we will know whether each student passed the course or not. Some data points are presented below:
Student ID | Hours studied | Pass/fail
-| - | - 
24 | 15 | Pass
41 | 9.5 | Pass
58 | 2 | Fail
101 | 5 | Fail
103 | 6.5 | Fail
215 | 6 | Pass

Based on the table, what kind of conclussion could you draw between the hours studied and passing the exam? We could think that if we have data from hundreds of students, maybe we could see the amount needed to study in order to pass the course. We can present this data in a chart as you can see below:

> ### exercise 19: logistic regression
>
> ![](images/10_7.PNG)
>
>Each dot on the figure corresponds to one student. On the bottom of the figure we have the scale for how many houws the student studied for the exam, and the students who passed the exam are showed as dots at the top of the chart, and the ones who failed are shown on the bottom. We'll use the scale on the left to indicate the predicted probability of passing, which we'll get from the logistic regression model as we explain just below. Based on this figure, you can see roughly that students who spent longer studying had better chances of passing the course. Especially the extreme cases are intuitive: with less than an hour's work, it is very hard to pass the course, but with a lot of work, most will be successful. But what about those taht spend time studying somewhere inbetween the extrems? If you study for 6 hours, what are your chances of passing?
>
>We can quantify the probability of passing using a logistic regression. The curve in the figure can be interpreted as the probability of passing: for example, after studying for five hours, the probability of passing is a little over 20%. We will not want to go into details on how to obtain hte curve, but it will be a similar to how we learned the weights in linear regression. 
>
>If you have an 80% chance of passing a university exam, based on the above figure, how many hour should you approximately study for?
>
>10-11 Hours - Correct. The other answers give roughly a 30%, a 50%, and a 70% chance of passing respectively. To have an 80% chance of passing, you should study for around 10-11 hours.

Logistic regression is also used in a great variety of real-world AI applications such as predicting financial risks, in medical studies and so on. However, like linear regression, it is also constrained by the linearity property and we need many other methods in our toolbox. We will return to the linearity issue later when we discuss neural networks.

### The limits of machine learning

To summarize, machine learning is a very powerful tool for building AI applications. In addition to the nearest neighbor method, linear regression, and logistic regression, there are literally hundreds, if not thousands, of different machine learning techniques, buy they all boil down the same thing: trying to extract patterns and dependencies from data and using them either to gain understanding of a phenomenon or to predict future outcomes.

Machine learning can be a cery hard problem and we can't usually achieve a perfect method that would always produce the correct label. However, in most cases, a good but not perfect prediction is still better than none. Sometimes we may be able to produce better predictions by ourselves but we still prefer to use machine learning because the machine will make its predictions faster and it will also keep churning out predictions without getting tired. Good examples are recommendation systems that need to predict what musci, what videos, or what ads are more likely to be of interest to you.

The factors that affect how good a result we can achieve include:

- The hardness of the task: in handwritten digit recognition, if the digits are written very sloppily, even a human can't always guess correctly what the writer intended.
- The machine learning method: some methods are far better for a particular task than others.
- The amount of training data: from only a few examples, it is impossible to obtain a good classifer.
- The quality of data.

> <h3>Data quality matters</h3>
>
> In the beginning of this chapter, we emphasizedthe importance of having enough data and the risks of overfitting. Another equally important factor is the **quality** of the data. In order to build a model that generalizes well to data outside of the training data, the training data needs to contain enough information that tells you what the image given to the algorithm is about, and you have trained it only on pictures of dogs and cats, it will assign everything it sees as either a dog or a cat. This would make sense if the algorithm is used in an enviroment where it will only see cats and dogs, but not if it is expected to see boats, cars, and flowers as well.
>
> We'll return to potential problems caused by "biased" data.

It is also important to emphasize that different machine learning methods are suitable for different tasks. Thus, there is no single best method for all problems ("one algorithm to rule them all..."). Fortunately, one can try out a large number of different methods and see which one of them works best in the problem at hand.

This leads us to a point that is very important but often overlooked in practice: what it means to work better. In the digit recognition taks, a good method would of course produce the correct label most of the time. We can measure this by the classification error: the fraction of cases where our classifier outputs the wrong class. In predicting apartment prics, the quality mneasure is typically something like the difference between the predicted price and the final price for which the apartment is sold. In amny real-life applications, it is also worse to err in one direction than in another: setting the price too high may delay the process by months, but setting the price too low will mean less money for the seller. And to take yet another example, failing to detect a pedestrian in fron of a car is a far worse error than falsely detecting one when there is none.

As mentioned above, we can't usually achieve zero error, but perhaps we will be happy with error less than 1 in 100 (or 1%). This too depends on the application: you wouldn't be happy to have only 99% safe cars on the streets, but being able to predict whether you'll like a bew song with that accuracy may be more than enough for a pleasant listening experience. Keeping the actual goal in mind at all times helps us make sure that we create actual added value.

## Recap

<h3>After completing chapter 4 you should be able to:</h3>

- Explain why machine learning techniques are used
- Distingish between unsupervised and supervised machine learning scenarios
- Explain the principles of three supervised classification methods: the nearest neighbor method, linear regression, and logistic regression.

# Chapter 05: Neural networks

<h3>Areas like natural language and image processing have traditionally been sore points of AI. Neural networks and deep learning are being used to achieve, significant improvements in these areas.</h3>

## I. Neural network basics

<h3>Our next topic, deep learning and neural networks tend to attract more interest than many of the other topics.</h3>

One of the reasons for the interest is the hope to understand our own mind, which emerges from neural processing in our brain. ANother reason is the advances in machine learning achieved within the recent years by combining massive data sets and deep learning techniques.

### What are neural networks?

To better understand the whole, we will start by discussing the individual units that make it up. A neural network can mean either a "real" biological neural network such as the one in your brain, or an artificial neural network simulated in a computer.

> <h3>Deep Learning</h3>
>
> Deep learning refers to certain kinds of machine learnign 
>
> Deep learning refers to certain kinds of machine learnign techniques where several "layers" of simple processing units are connected in a network so that the input to the system is passed through each one of them in turn. This architecture has been inspired by the processing of visual information in the brain coming through the eyes and captured by the retina. This depth allows the network to learn more complex structures without requiring unrealistically large amounts of data.
>
> <h3>Neurons, cell bodies, and signals</h3>
>
>A neural network, either biological and artificial, consists of a large number of simple units, neurons, that receive and transit signals to each other. The neurons are very simple processors of information, consistning of a cell body and wires that connect the neurons to each other. Most of the time, they do nothing but sit still and watch for signals coming in through the wires.
>
> <h3>Dentrites, axons, and synapses</h3>
> In the biological lingo, we call the wires that provide the input to the neuronal dendrites. Sometimes, depending on the incoming signals, the neuron may fire and send a signal out for the other neurons to receive. The wire that transmits the outgoing signal is called an axon. Each axon may be connected to one or more dentrites at intersections that are called synapses.

Isolated from its fellow-neurons, a single neuron is quite unimpressive, and capable of only a very restricted set of behaviors. When connected to each other, however, the system resulting from their concerted action can become extremely complex. To find evidence of this, look no further than (to use legal jargon) "Exhibit A": your brain! The behaviour of the system is determined by the ways in which the neurons are wired together. Each neacts to the incoming signals in a specific signals in a specific way that can also adapt over time. This adaptation is known to be the key to functions such as memory and learning. 

### exercise20: elements of a neural network

Label the different components of a neuron into the diagram below. Hint: The input pf the neuron comes from the left and the output goes to the right.

![](images/11_1.svg)

D -> Synapse (connection)

B -> Dentrite

A -> Cell body

C -> Axon (output)

### Why develop artificial neural networks? 

THe purpose of building artificial models of the brain can be neuroscience, the study of the brain and the nervous system in general. It is tempting to think that by mapping the human brain is enough in detail, we can discover the secrets of human and animal cognition and consciousness.

![](images/11_2.svg)

> <h3>Modeling the brain</h3>
>
>[The BRAIN initiative](https://www.braininitiative.nih.gov/) led by American neuroscience researchers is pushing forward technologies for imaging, modeling, and simulating the brain at finer and larger scale than before. Some brain research projects are very ambitious in terms of objectives. [The Human Brain Project](https://www.youtube.com/watch?v=JqMpGrM5ECo) promised in 2012 that "the mysteries of the mind can be solved - soon". After years of work, the Human Brain Project was facing questions about when the [billion euros invested by the European Union](https://www.scientificamerican.com/article/why-the-human-brain-project-went-wrong-and-how-to-fix-it/) will deliver what was promised, even though, to be fair some less ambitious milestones have been achieved.

However, ecen while we seem to be almost as far from understanding the mind and consicousness, there are clear milestones that have been achieved in neuroscience. By better understanding of the structure and function of the brain, we are already reaping some concrete rewards. We can, for instance, identify abnormal functioning and try to help the brain avoid them and reinstate normal operation. This can lead to life-changing new medical treatments for epople suffering from neurological disorders: epilepsy, Alzheimer's disease, problems caused by developmental disorders or damage caused by injuries, and so on.

> <h3>Looking to the future: brain computer interfaces</h3>
>
>One research direction in neuroscience is brain-computer interfaces that allow interacting with a computer by simply thinking. The current interfaces are very limited and they can be used, for example, to [reconstruct on a very rough level what a person is seeing](), or to [control robotic arms or drones by thought](). Perhaps some day we can actually implement a thought reading machine that allows precie instructions byt currently they belong to science fiction. It is also conceivable that we could feed information into the brain by stimulating it by small electrical pulses. Such stimulation is currently used for theurapeutic purposes. Feeding detailed information such as specific words, ideas, memories, or emotions is at least currently science fiction rather than reality, but obviously we know neither the limits of such technology, nor how hard is to reach them.

We've drifted a little astray from the topic of the ocurse. In fact, another main reason for building artificial networks has little to do with understanding biological systems. It is to use biological systems as an inspiration to build better AI and machine learning techniques. THe idea is very natural: the brain is an amazingly complex information processing system capable of a wide range of intelligent behaviors (plus occasionally some not-so-intelligent ones), and therefore, ti makes sense to look for inspiration in it when we try to create artificially intelligent systems.

Neural networks have been a major trend in AI since the 1960s. We'll return to the waves of popularity in the history of AI in the final part. Currently neural netowrks are again at the very top of the list as deep learning is used to achieve significant improvements in many areas such as natural language and image processing, which have traditionally been sore points of AI.

### What is so special about neural networks?

THe case for neural networks in general as an approach to AI is based on a similar argument as that for logic-based approaches. In the latter case, it was though processes, and in particular, manipulation of symbols representing certain concrete or abstract concepts using logical rules.

The argument for neural networks is that by simulating the lower-level, "subsymbolic" data processing on the level of neurons and neural networks, intelligence will emerge. THis all sounds very reasonable, but keep in mind that in order to build flying machines, we don't build airplanes that flap their wings, or that are made of nomes, muscle, and feather. Likewise, in artificial neural networks, the internal mechanism of the neurons is usually ignored and the artificial neurons are often much more simpler than their natural counterparts. The electro-chemical signaling mechanisms between natural neurons are also mostly ignored in artificial models when the goal is to build AI systems rather than to simulate biological systems.

Compared to how computers traditionally owrk, neural netowrks have certain special features:

1. Neural network key feature

    For one, in a traditional computer, information is processed in a central processor (aptly named the central processing unit, or CPU for short) which can only focus on doing one thing a a time. The CPU can retrieve data to be processed from the computer's memory, and store the result in the memory. Thus, data storage and processing are handled by two separate components of the computer: the memory and the CPU. In neural networks, the system consists of a large number of neurons, each of which can process information on its own so that instead of having a CPU process each piece of information one after the other, the neurons process vast amounts of information simultaneously.

2. Neural network key feature

    The second difference is that data storage (memory) and processing isn't separated like in traditional computers. The neurons both store and process information so that there is no need to retrieve data from the memory for processing. The data can be stored short term in the neurons themselves (they either fire or not at any given time) or for longer term storage we will discuss below.

Because of these differences, neural networks and traditional computes are suited for somewhat different tasks. Even though it is entirely possible to simulate neural networks in traditional computers, which was the way they were used for a long time, their maximum capacity is achieved only when we use special hardware (computer devices) that can process many pieces of information at the same time. This is called **parallel processing**. Incidentally, graphics processors (or graphics processing units, GPUs) have this capability and they have become a cost-effective solution for running massive deep learning methods.

## II. How neural networks are built

<h4>As we said earlier, neurons are very simple processing units. Having discussed linear and logistic regression in Chapter 4, the essential technical details of neural networks can be seen as slight variations of the same idea.</h4>

><h3>Weights and inputs</h3>
>
>The basic artificial neuron model involves a set of adaptive parameters, called weights like in linear and logistic regression. Just like in regression, these weights are used as multipliers on the inputs of the neuron, which are added up. The sum of the weights times the inputs is called the linear combination of the inputs. You can probably recall the shopping bill analogy: you multiply the amount of each item by its price per unit and add up to get the total.

If we have a neuron with six inputs (analogous to the amounts of the six shopping items: potatoes, carrots, and so on), input1, input2, input3, input4, input5, and input6, we also need six weights. The weights are analogous to the prices of the items. We'll call them weight1, weight2, weight3, weight4, weight5, and weight6. In addition, we'll usually want to include an intercept term like we did in linear regression. This can be thought of as fixed additional charge due to processing a credit card payment, for a example.

We can then calculate the linear combination like this: linear combination = intercept + weight1 * input1 + ... + wight6 * input6 (where the ... is a shorthand notation meaning that the sum inclue all the terms from 1 to 6).

With some example numbers we could then get:

> 10.0 + 5.4 * 8 + (-10.2) * 5 + (-0.1) * 22 + 101.4 * (-5) + 0.0 * 2 + 12.0 * (-3) = -543.0

### exercise21: weights and input

In this exercise, consider the following expression that has both weights and inputs: 10.0 + 5.4 * 8 + (-10.2) * 5 + (-0.1) * 22 + 101.4 * (-5) + 0.0 * 2 + 12.0 * (-3) = -543.0

- What is the intercept term in the expression? B -> 10.0: Correct. The intercept is the number in the equation that is not multiplied by any variable.

- What are the inputs? A -> 8, 5, 22, -5, 2, -3: Correct. Compare the equation in the exercise to the one above in the definition: we defined the linear combination to be intercept + weights x inputs, so the inputs are the second numbers in the multiplication.

- Which of the inputs needs to be changed the least to increase the output by a certain amount? D -> fourth: Correct. The fourth weight is the largest one. To increase the output by some predetermined amount, the fourth input would have to be increased the least.

- What happens when the fifth input is incremented by one? A -> nohting (C -> The output increases by two) Incorrect. The weight for the fifth input is 0.0, which means that no matter what value the fifth input has, its effect on the linear combination is always zero.

The weights are almost learned form data using the same ideas as in linear or logistic regression, as discussed previously. But before we discuss this in more detail, we'll introduce another important stage that a neuron completes before it sends out an output signal.

### Activations and outputs

Once the linear combinatiosn has been computed, the neuron does one more operation. It takes the linear combination and puts it through a so-called activation function. Typical examples of the activation function include:

- identity function: do nothing and just output the linear combination

- step function: if the value of the linear combination is greater than zero, send a pusle (ON), otherwise fo nothing (OFF).

- sigmoid function: a "soft" version of the step function.

Note that with the first activation fucntion, the identity function, the neuron is exactly the same as linear regression. This is why the identify fucntion, the neuron is exactly the same as linear regression. This is why the identify function is rarely used in neural networks: it leads to nothing new and interesting.

><h3>How neurons activate</h3>
>
>Real, biological neurons communicate by sengind out sharp, electrical pulses called "spikes", so that at any given time, their outgoing signal is either on or off (1 or 0). THe step function, imitates this behavior. However, artificial neural networks tend to use activation functions that output a continous numerical activation level at all times, such as the sigmoid function. Thus to use a somewhat awkward figure of speech, real neurons communicate by something similar to the Morse code, whereas artificial neurons communicate by adjusting the pitch of their voice as if yodeling.

![](images/12_1.svg)

The output of the neuron, determined by the linear combination and the activation function, can be used to extract a prediction or decision. For example, if the network is designed to identify a stop sign in fornt of a self-driving car, the input can be the pisxels of an image captured by a camera attached in front of the car, and the output can be used to activate a stopping procedure that stops the car before the sign.

Learning or adaptation in the network occurs when the weights are adjusted so as to make the network produce the correct outputs, just like in linear or logisitic regression. Many neural networks are very large, and the largest contain hundreds of billions of wights. Optimizing them all can be daunting task that requires massive amounts of computing power.

### exercise22: Activations and outputs

Below are graphs for three dofferent activations functions with different properties. First we have the sigmoid function, then the steps function, and finally the identity function. IMPORTANT: Nothe the different y-axis (vertical) scale in the identity function chart.

![](images/12_2.jpeg)

![](images/12_3.jpeg)

![](images/12_4.jpg)

Which of the activations described above gives:
- the highest output for an input of 5? 
    
    Identity -> Correct. The identity function will give an output of 5 for an input of 5. The sigmoid will output something very close to 1, and the step function will output exactly 1. 

- the lowest output for an input of -5?

    Identity -> Correct. The identity function will give an output of -5 for an input of -5. The sigmoid will output something very close to 0, and the step function will output exactly 0. 

- the highest output for an input of -2.5?

    Sigmoid -> Correct. For an input of -2.5, the identity function will output -2.5, and the step function will output 0. The sigmoid function will output something that is higher than 0 but lower than 0.1.

### Perception: the mother of all ANNs

The perception is simply a fancy name for the simple neuron model with the step activation function we discussed above. It was among the very first formal models of neural computation and because of its fundamental role in the history of neural networks, it wouldn't be unfair to call it the "mother of all artificial neural networks".

It can be used as a simple classifier in binary classification tasks. A method for learning the weights of the perceptron from data, called the Perceptron algorithm, was introduced by the psychologist Frank Rosenblatt in 1957. We will not study the Perceptron algorithm in detail. Suffice to say that is just about as simple as the nearest neighbor classifier. The basic principle is to feed the network training data one example at a time. Each misclassification to an update in the weight.  

><h3>AI hyperbole</h3>
>
>After its discovery, the Perceptron algorithm received a lot of attention, not least because of optimistic statements made by its inventor, Frank Rosenblatt. A classic example AI hyperbole is a New York Times article published on July 8th, 1958: "The Navy revealed the embyro of an electronic computer today that it expects will be able to walk, talk, see, reproduce itself and be conscious of its existence."
>
>Please note that neural network enthusiasts are not at all the only ones inclined towards optimism. The rise and fall of the logic-based expert systems approach to AI had all the same hallmark features of an AI-hype and people claimed that the final breakthrough is just a shorth while away. The outcome both in the early 1960s and late 1980s was a collapse in the research funding called an AI Winter.

The history of the debate that eventually lead to almost complete abandoning of the neural network approach in the 1960s for more than two decades is extemly fascinating. The article *[A Sociological Study of the Official History of the Perceptrons Controversy](http://journals.sagepub.com/doi/10.1177/030631296026003005)* by Mikel Olazaran (published in *Social Studies of Science*, 1996) reviews the events from a sociology of science point of view. Reading it today is quite thought provoking. Reading stories about celebrated AI heroes who had develop neural networks algorithms that would soon reach the level of human intelligence and become self-conscious can be compared to some statements made during the current hype. If you take a look at the above article, even if you wouldn't read all of it, it will provide an interesting backgorund to today's news. Consider for example an [article in the MIT Technology Review](https://www.technologyreview.com/s/608911/is-ai-riding-a-one-trick-pony/) published in September 2007, where Jordan Jacobs, co-founder of a multimillion dollar Vecotr institute for AI compares Geoffrey Hinton (a figure-head of the current deep learning boom) to Einstein because of his constributions to development of neural network algorithms in the 1980s and later. Also recall the Human Brain project mentioned in the previous section.

According to Hinton "the fact it doesn't work is just a temporary annoyance" (although according to the article, Hinton is laughing about the above statement, so it's hard to tell how seriours he is about it). The Human Brain project claims to be ["close to a profound leap in our understanding of consciousness"](https://www.humanbrainproject.eu/en/follow-hbp/news/the-quest-for-consciousness/). Doesn't that sound familiar?

Noone really knows the future with certainty, but knowing the track record of earlier announcements of imminent breakthroughs, some critical thinking is advised. We'll retrun to the future of AI in the final chapter, but for now, let's see how artificial neural networks are built.

### Putting neurons together: networks

A single neuron would be way too simple to make decisions and prediction reliably in most real-life applications. To unleash the full potential of neural networks, we can use the output of one neuron as the input of other neurons, whose outputs can be the input to yet other neurons, and so on. The output of the whole network is obtained as the output of a certain subset of the neurons, which are called the output layer. We'll return to this in a bit, after we discussed the way neural networks adapt to preduce different behaviors by learning their paramenters from data.

><h3>Layers</h3>
>
>Often the network architecture is composed of layers. The input consists of neurons that get their inputs directly fro mthe data. So for example, in an image recognition task, the input layer would use the pixel values of the input image as the inputs of the input layer. The network typically also has hidden layers that use the other neurons' outputs as their input, and whose output of the whole network. All the neurons on a given layer get inputs from neurons on the previous layer and feed their output to the next.

A classical example of a multiplayer network is the so-called multiplayer perceptron. As we discussed above, Rosenblatt Perceptron algorithm can be used to learn the wights of perceptron. For multilayer perceptron, the corresponding learning problem is way harder and it took a long time before a working solution was discovered. But eventually, one was invented: the backpropagation algorithm led to a revival of neural networks in the late 1980s. It is still at heart of many of the most advanced deep learning solutions.

><h3>Meanwhile in Helsinki...</h3>
>
>The path(s) leading to the backrpropagation are rather long and winding. An interesting part of the history is related to the computer science department of the University of Helsinki. About three years after the founding of the department 1967 [a Master's thesis](http://people.idsia.ch/~juergen/linnainmaa1970thesis.pdf) was written by a student called Seppo Linnainmaa. The topic of the thesis was "Cumulative rounding error algorithms as a Taylor approximation of individual rounding errors" (the thesis was wirtten in Finnish, so this is a translation of the actual title "Algoritmin kumulatiivinen pyöristysvirhe yksittäisten pyöristysvirheiden Taylor-kehitelmänä").
>
>The automatic differentiation method developed in the thesis was later applied by other researchers to quantify the sensitivity of the output of a multilayer neural network with respect to the individual weights, which is the key idea in backpropagation.

### A simple neural network classifier

To give relatively simple example of using a neural network classifier, we'll consider a task that is very similar to the MNIST digit recognition task, namely classifying images in two classes. We will first create a classifier to classify whether an image shows a cross (x) or a circle (o). Our images are represented here as pixels that are either colored or white and the pixels are arranged in 5 * 5 grid. In this format our images of a cross and a circle (mor like a diamond, to be honest) look like this:

![](images/12_5.png)

In order to build a neural network classifier, we need to formalize the problem in a way where we can solve ir using teh methods we have learned. Our first step is to represent the information in the pixels by numerical values that can be used as the input to a classifier. Let's use 1 if the square is colored, and 0 if it is white. Note that although the symbols in the above graphic are of different color (green and blue), our classifier will ignore the color information and use only the colored/white information. The 25 pixels in the image make the inputs of our classifier.

To make sure that we know which pixel is which in the numerical representation, we can decide to list the pixels in the same order as you'd read text, so row by row from the top, and reading each row from left to right. The first row of the cross, for example, is represented as 1,0,0,0,1; the second row as 0,1,0,1,0, and so on. THe full input for the corss is then: 1,0,0,0,1,0,1,0,1,0,0,0,1,0,0,0,1,0,1,0,1,0,0,0,1.

We'll use the basic neuron model where the first step is to compute a linear combination of the inputs. Thus need a weight for each of the input pixels, which means 25 weights in total.

Finally, we use the step activation function. If the linear combination is negative, the neuron activation is zero, which we decide to use to signify a cross. If the linear combination is positive, the neuron is one, which we decide to signify a circle.

Let's try what happens when all weights take the same numerical value, 1. With htis setup, our linear combination for the cross image will be 9 (9 colored pixels, so 9 * 1, and 16 white pixels, 16 * 0), and for the circle image it will be 8 (8 colored pixels, 8 * 1 and 17 white pixels, 17 * 0). In other words, tthe linear combination is positive for both images and they are thus classified as circles. Not a very good result given that there are only two images to classify.

To improve the result, we need to adjust the weights in such a way that the linear combination will be negative for a cross and positive for a circle. If we think about what differentiates images of crosses and circles, we can see that circles have no colred pisxels in the center of the image, whereas crosses do. Likewise, the pixels at the corners of the image are colored in the cross, but white in the circle.

We can now adjust the weights. There are an infinite number of weights that fo the job. For example, assign weight -1 to the center pixel (the 13th pixel), and weight 1 to the pixels in the middle of each of the four sides of the image, letting all the other weights be 0. Now, for the cross input, the center pixel produce the value -1, while for all the other pixels either the pixel value or the weight is 0, so that -1 is also the total value. This leads to activation 0, and the cross is correctly classified.

How about the circle then? Each of the pixels in the middle of the sides produces the value 1, which males 4 * 1 = 4 in total. For all the other pixels either the pixel value or the weight, so 4 is the total. Since 4 is a positive value, the activation is 1, and the circle is correctly recognized as well.

### Happy or not?

We will now follow similar reasoning to build a classifier for smiley faces. You can assign weights to the input pixels in the image by clicking on them. Clicking once sets the weight to 1, and clicking again sets it to -1. The activation 1 indicates that the image is classified as a happy face. Which can be correct or not, while activation -1 indicates that the iamge is classified as a sad face.

Don't be discouraged by the fact that you will not be able to classify all the smiley faces correctly: it is in fact impossible with our simple classifier! This one important learning objective: sometimes perfect classification just isn't possible because the classifer is too simple. In this case the simple neuron that uses a linear combination of the inputs is too simple for the task. Observe how you can build classifiers that work well in different cases: some classify most of the happy faces correctly while being worse for sad faces, or the other way around.

Can you achieve 6/8 correct for both happy and sad faces?

![](images/12_6.png)

## III. Advanced neural network techniques

<h4>In the previous section, we have discussed the basic ideas behind most neural network methods: multilayer networks, non-linear activation functions, and learning rules such as the backpropagation algorithm.</h4>

They power almost all modern neural network applications. However, there are some interesting and powerful varaitions od the theme that have led to great advances in deep learning in many areas.

### Convolutional neural networks (CNNs)

One area where deep learnign has achieved spectacular success is image processing. The simple classifier what we studied in detail in the previous section is severely limited - as you noticed it wasn't even possible to classify all the smiley faces correctly. Adding more layers in the network and using backpropagation to learn the weights does in principle solve the problem, but another one emerges: the number of weights becomes extremely large and consequently, the amount of training data requiered to achieve satisfactory accuracy can become too large to be realistic.

Fortunately, a very elegant soluttion to the problem of too many weights exists: a special kind of neural network, or rather, a special kind of layer that can be included in a deep neural networl. This special kind of layer is a so-called **convolutional layer**. Networks including convolutional layers are called **convolutional neural networks** (CNNs). Their key property is that they can detect image features such as bright or dark (or specific color) spots, edges in various orientations, patterns, and so on. These form the basis for detecting more abstract features such as a cat's ears, a dog's snout, a person's eye, or the octogonal shape of a stop sign. It would normally be hard to train a neural network to detect such features based on the pixels of the input image, because the features can appear in different positions, differenct orientations, and in different sizes in the image: moving the object or the camera angle will change the pixel values dramatically even if the object itself looks just the same to us. In order to learn to detect a stop sign in all these differenct conditions would require wast of amounts of trainign data because the network would only detect the sign in conditions where it has appeared in the training data. So, for example, a stop sign in the top right corner of the image would be detected only if the training data included an image with the stop sign in the top right corner. CNNs can recogniza the object anywhere in the images no matter where it has been observed in the training images.

><h3>Why we need CNNs</h3>
>
>CNNs use a clever trich to reduce the amount of training data required to detect objects in different conditions. The trick basically amounts to using the same input weights for many neurons - so that all of these neurons are activated by the same pattern - but with a different input pixels. We can for example  have a ser of neurons that are activated by a cat's pointy ear. When the input is a photo of a cat, two neurons are activated, one for the left ear and one for the right. We can also let the neuron's input pixels be taken from a smaller or a larger area, so that different neurons are activated by the ear appearing in different scales (sizes), so that we can detect a small cat's ears even if the training data only included images of big cats.

The convolutional neurons are typically placed in the bottom layers of the network, which processes the raw input pixels. Basic neurons (like the perceptron neuron discussed above) are placed i nthe higher layers, which process the output of the bottom layers. The bottom layers can usually be trained using unsupervised learnign, without a particular predictiontask in mind. Their weight will be tuned to detect features that appear frequently in the input data. Thus, with photos of animals, typical features will be ears and snouts, whereas in images of buildings, the features are architectural components such as walls, roofs, windows, and so on. If a mix of various objects and scenes is used as the input data, then the features learned byt the bottom layers will be more or less generic. This means that pre-trained convolutional layers can be reused in many idderent image processing tasks. This is extremely important since it is easy to get virtually unlimited amounts of unlabeled training data - images without labels - which can be used to train the bottom layers. The top layers are always trained by supervised machine learnign techniques such as back propagation.

![](images/13_1.svg)

### Do neural networks dream of electric sheep? Generative adversarial networks (GANs)

Having learned network from data, it can be used for prediciton. Sicne the top layers of the network have been trained in a supervised manner to perform a particular classification task, the top layers are really useful only for that task. A network trained to detect stop signs is useless for detecting handwritten digits or cats.

A fascinating is obtained by taking the pre-trained bottom layers and studying what the features they have learned look like. This can be achieved by generating images that activate a certain set of neurons in the  bottom layers. Looking at the generated images, we can see what the neural networks "thinks" a particular feature looks like, or what an image wihth a select set of features in it would look like. Some even like, or what an image with a select set of features in to would look like. Some even like to talk about the networks "dreaming" or "hallucinating" images (see Google's [DeepDream system](https://en.wikipedia.org/wiki/DeepDream)).

><h3>Be careful with metaphors</h3>
>
>However, we'd like to obce again emphasize the problem with metaphors such as dreaming when simple when simple optimization of the input image is meant - remember the suicase words discussed in Chapter 1. The neural network doesn't really dream, and it doesn't have a concept of a cat that would understand in a similar sense as a human understands. It is simply trained to recognize objects and it can generate images that are similar to the input that it is trained on.

To actually generate real looking cats, human faces, or other objects (you'll get whatever you used as the training data), [Ian Goodfellow](https://en.wikipedia.org/wiki/Ian_Goodfellow) who currently works at Google Brain, proposed a clever combination of two neural networks. THe idea is to let the two networks compete against each other. One of the networks is trained to generate images like the ones in the training data. THe other network's task is to separate images generated by the first network from real images from the training data - it is called the adversarial network, and the whole system is called generative adversarial network or a GAN.

THe system trains the two models side by side. In the beginning of the training, the adversarial model has an easy task to tell apart the real images from the training data and the clumsy attempts by the generative model. However, as the generative network slowly gets better and better, the adversarial model has to improve as well, and the cycle continues until eventually the generated images are almost indistinguishable from real ones. The GAN tries to not only reproduce the images in the training data: that would be a way too simple strategy to beat the adversarial network. Rather, the system is trained so that it has to be able to generate new, real-looking images too.

![](images/13_2.jpg)

The above images were generated by a GAN developed by NVIDIA in a project led by [Prof Jaakko Lehtinen](https://users.aalto.fi/~lehtinj7/) (see [this article for more details](https://www.technologyreview.com/the-download/609290/meet-the-fake-celebrities-dreamed-up-by-ai/)).

Could you have recognized them as fakes?

## Recap

<h4>After completing Chapter 5 you should be able to:</h4>

- Explain what a neural network is and where they are being succesfully used.

- Understand the technical methods that underpin neural networks

# Chapter 06: Implications

## I. About predicting the future

<h3>We will start by addressing what is known to be one of the hardest problems of all: predicting the future.</h3>

You may be disappointed to hear this, but we don't have a crystal ball that would show us what the world will be like in the future and how AI will transform our lives.

As scientist, we are often asked to provide predictions, and our refusal to provide any is faced with  roll on the eyes ("boring academics"). But in fact, we claim that anyone who claims to know the future of AI and the implications it will have on our society, should be treated with suspicion.

![](images/14_1.svg)

### The reality distortion field 

Not everyone is quite as conservative about their forecasts, however. In the modern world where big headlines sell, and where you have to dissect news into 280 characters, reserced (boring?) messages are lost, and simple and dramatic messages are magnified. In the public perception of AI, this is clearly true.

><h3>From utopian visions to grim predictions</h3>
>
>The media sphere is dominated by the extremes. We are beginning to see AI celebrities, standing for one big idea and making oracle-like forecasts about the future of AI. The media love their clear messages. SOmepromise us a [utopian future with exponential growth](https://www.youtube.com/watch?v=AIQ981NoZmk) and trillion-dollar industries emerging out of nowhere, [true AI that will solve all problems](https://www.youtube.com/watch?v=-Y7PLaxXUrs) we cannot solve by ourselves, and where [humans don't need to work at all](https://www.youtube.com/watch?v=9Jxlx9SZEAk).
>
>It has also been claimed that [AI is a path of world domination](https://www.youtube.com/watch?v=xPuAzc3Y_64). Others make even more extraordinary statemnents according to which [AI marks the end of humanity](https://www.youtube.com/watch?v=JYlKrHzknBE) (in about 20-30 years now), [life itself will be transformed](https://www.youtube.com/watch?v=oYmKOgeoOz4) in the "Age of AI", and that [AI is a threat to our existence](https://youtu.be/xs_HhZrCBdg).

While some forecasts will probably get at least something right, others will likely be useful only as demonstrations of how hard is to predict, and many don't make much sense. What we would like to achieve is for you to be able to look at these and other forecasts. and be able to critically evaluate them.

### On hedgehogs and foxes

The political scientist [Phillip E. Tetlock](https://en.wikipedia.org/wiki/Philip_E._Tetlock), author of *Superforecasting: The Art and Science of Prediction*, classifies people into two categories: those who have one big idea ("hedgehogs"), and those thow have many small ideas ("foxes"). Tetlock has carried out an experiment between 1984 and 2003 to study factors that could help us identify which predictions are likely to be accurate and which are not. One of the significant findings was that fixes tend to be clearly better at prediction than hedgehogs, especially when it comes to long-term forecasting.

Probably the mesages that can be expressed in 280 characters are more often big and simple hedgehog ideas. Our advice is to pay attention to carefully balanced information sources, and to be suspicious about people who keep explainin everythin using a single argument.

Prediction the future is hard but at least we can consider the past and present of AI, and by understanding them, hopefully be better prepared for the future, whatever it turns out to be.

![](images/14_2.svg)

### AI Winters

The history of AI, just like many others fields of science, has witnessed the coming and going of various different trends. In philosophyu of science, the term used for a trend is paradigm. Tipically, a particular paradigm is adopted by most of the research community and optimistic predictions about progres in the near-future are provided. For example, in the 1960s neural networks were widely believed to solve all AI problems by imitationg the learning mechanisms in nature, the human brain in particular. The next big thing was expert systems based on logic and human-coded rules, which was the dominant paradigm in the 1980s.

### The cycle of hype

In the beginning of each wave, a number of early success stories tend to make everyone happy and optimistic. The success stories, even if they may be in restricted domains and in some wways incomplete, become the focus on public attention. Many researchers ruch into AI - or at least calling their research AI - in order to access the increased research in funding. Companies aslo initiate and expand their efforts in AI in the fear of missing out (FOMO).

So far, each time an all-encompasing, general solution to AI has been said to be within reach, progress has ended up running into insumountable problems, which at the time were thought to be minor hiccups. In the case of neural networks in the 1960s, the hiccups were related to handling nonlinearities and to solving the machine learning problems associated with the increasing number of parameters required by neural network architectures. In the case of expert system in the 1980s, the hiccups were associated with handling uncertainty and common sense. As the true nature of the remianing problems dawned after years of struggiling and unsatidfied promises, pessimism about the paradigm accumulated and an AI winter followed: interest in the filed faltered and research efforts were directed elsewhere.

### Modern AI

Currently, roughly since the turn of the millenium, AI has been on the rise again. Modern AI mehtods turn to focus on breaking a problem into a number of smaller, isolated and well-defined problems and solving one at a time. Modern AI is bypassing grand questions about meaning of intelligence, the mind, and consciousness, and focusing on building useful solutions in real-world problems. Good news for us all who can benefit from such solutions!

Another characteristic of modern AI methods, closely related to working in the complex and "messy" real world, is the ability to handle uncertainty, which we demonstrated by studying the uses of probability in AI in Chapter 3. Finally, the current upwards trend of AI has been greatly boosted by the come-back neural networks and deep learning techniques capable of processing images and other real-world data better than anything we have seen before.

><h3>So are we in a hype cycle?</h3>
>
>Whether the history will reppeat itself, and the current boom will be once again followed by an AI winter, is a matter that only time can tell. Even if it does, and the progress towards better and better solutions slows down to a halt, the significance of AI in the society is going to stay. Thanks to the focus on useful solutions to real-world problems, modern AI research yields fruit already today, rather than trying to solve the big questions about general intelligence first - which was where the earlier attempts failed.

### Prediction 01: AI will continue to be all around us

As you recall, we started by motivating the study of AI by discussing prominent AI appplications by discussing prominent AI applications that affects all our lives. We highlighted tree examples: self-driving vehicles, recommendation systems, and image and video processing. During the course, we have also discussed a wide reange of other applications that contribute to the ongoing technological transition.

><h3>AI making a difference</h3>
>
>As a consequence of focusing on practicality rather than the big problems, we live our life sorrounded by AI (even if we may most of the time be happily unaware of it): the music we listen to, the products we buy online, the movies and series we watch, our routes of trasportation, and even the news and information that we have available, are all influenced more and more by AI. What is more, basically any field of science, from medicine and astrophysics to medieval history, is also adopting AI methods in order to deepen our understanding of the universe and of ourselves.

![](images/14_3.svg)

### Prediction 02: The Terminator isn't coming

One of the most pervasive and persistent ideas related to the future of AI is the Terminator. In case you should have somehow missed the image of a brutal humanoid robot with a metal skeleton and glaring eyes..., well that's what it is. *The Terminator* is a 1984 film by director James Cameron. In the movie, a global AI-powered defense system called Skynet becomes conscious of its existence and wipes most of the humankind out of existence with nukes and advanced killer robots.

><h3>Two doomsday scenarios</h3>
>
>There are two alternative scenarios taht are suggested to lead to the coming of the Terminator or other similarly terrifying forms of robot uprising. In the first, which is the story from the 1984 film, a powerful AI system just become conscious and decides that it just really, really dislikes humanity in general.
>
>In the second alternative scenario, the robot is controlled by an intelligent byt not conscious AI system that is in principle in human control. The system can be programmed, for example, to optimize the production of paper clips. Sounds innocent enough, doesn't it?
>
>However, if the system possesses superior intelligence, it will soon reach the maximum level of paper clip production that the available resources, such as energy and raw materials, allow. After this, it may come to the conclusion that it needs to redirect more resources to paper clip production. In order to do so, it may need to prevent the use of the resources for other purposes even if they are essential for human civilization. The simplest way to achieve this is to kill all hum,nas, after which a great deal more resources become available for the system's main task, paper clip production.

### Why these scenarios are unrealistic

There are a number of reasosn why both of the above scenarios are extremely unlikely and belong to science fiction rather than serious speculations of the future of AI.

#### Reason 1

Firstly, the idea that a **superintelligent**, conscious AI that outsmart humnas emerges as an unintended result of developing AI methods is naive. As you have seen in the previous chapters, AI methods are nothing but automated reasoning, based on the combination of perfectly understandable principles and plenty of input data, both of which are provided by humans or systems deployed by humans. To imagine that the nearest neighbot classifier, linear regression, the AlphaGo game engine, or even a deep neural network cvould become conscious and start evolving into a superintelligent AI mind requieres a (very) lively imagination.

Note that we are not claining that building human-level intelligence would be categorically impossible. You only need to look need to look as far as the mirror to see a proof of the possibility of a highly intelligent physical system. To repeat what we are saying: superintelligence will not emerge from developing narrow AI methods and applying them to solve real-world problems (recall the narrow vs general AI from the section on the philosophy of AI in Chapter 1).

#### Reason 2

Secondly, one of the favorite ideas of those who believe in superintelligent AI is the so called **singularity**: a system that optimizes and "rewires" itself so that it can improve its own intelligence at an ever accelerating, exponential rate. Such superintelligence would have humankind so far behind that we become like ants that can be exterminated without hesitation. The idea of exponential intelligence increade is unrealistic for the simple reason that even if aa system could optimize its own workings, it would keep facing more and more difficult problems that would slow ddown its progress, quite like the progress of human scientists requires ever greater efforts and resources by the whole research community and indeed the whole society still has the power to decide what we use technology, even AI technology, for. Much of this power is indeed gven to us by technology, so that every time we make progress in AI technology, we become more powerful and better at controlling any potential risk due to it.

><h3>The value alignment problem</h3>
>
>The paper clip example is known as the value alignment problem: specifying the objectives of the system so that they are aligned with out values is very hard. However, suppose that we create a superintelligent system that could defeat humans who trie to interfere with its work. It's reasonable to assume that such a system would also be intelligent enough to realize that when we say "make me paper clips", we don't really mean to turn the Earth into a paper clip factory of a planetary scale.

### Separating stories from reality

All in all, the Terminator is a great story to make movies but hardly a real problem worth panicking about. The Terminator is a gimmick, an easy way to get a lot of attention, a poster boy for journalists to increase click rates, a red herring to divert attention away from perhaps boring, but real, threats like nuvlcear weapons, lack of democracy, environmental catastrophes, and climate change. In fact, the real threat the Terminator poses is the diversion of attention from the actual problems, some of which involve AI, and many of which don't. We'll discuss the problems posed by AI inwhat follows, but the bottom line is: forget bout the Terminator, there are much more important things to focus on.

### exercise23: what is the perception of AI?

For this exercise, we want you to think about how AI is portrayed. Do an online **image search** for the term "AI" and see what kinds of pictures come up. If you are using Google search, you should choose "Images" in the top of the screen. 

What's the general impression you get about AI from the image search results? Is this an accurate representation of AI?

    For the search of images with the term "IA", the results are basically robot related images or images that can be assumed as neural networks.
    It doesn't seem to be an accurate representation of AI, as it still has a more abstract support than a physical support - aka robots. I think AI is quite complicated to illustrate, as we normally have the misconception of assuming that it needs to be a robot, but right now AI could be better portrayed more like ChatGPT. 
    However, illustrating AI as a diagram of a neural network I think it could be more appropriate, as it is what its trying to emulate.

## II. The societal implications of AI

<h4>In the very beginning of this course, we briefly discussed the importanc of AI in today's and tomorrow's society but at that time, we could do so only to a limited extent because we hadn't intorduced enough of the technical concepts and methods to ground the discussion on concrete terms.</h4>

Now that we have a better understanding of the basic concepts of AI, we are in a much better position to take part in rational discussion about the implications of already the current AI.

![](images/15_1.svg)

### Implication01: Algorithm bias

AI, and in particular, machine learning, is being used to make important decisions in many secotrs. This brings up the concept of algorithm bias. What it means is the embedding of a tendency to discriminate according ethnicity, gender, or other factors when maiking decisions about job applications, bank loans, and so on.

><h4>Once again, it's all about the data</h4>
>
>The main reason for algorithmic bias is human bias in the data. For example, when a job application filtering tool is trained on decisions made by humans, the machine learning algorithm may learn to discriminate against women or individuals with a certain ethnic background. Notice that this may happen even if ethnicity or gender are excluded from the data since the algorithm will be able to exploit the information in the applicant's name or address.

Algorithmic bias isn't a hypotthetical threat conceived by academid researchers. It's a real phenomenon that is already affecting people today.

#### Online advertising

It has been noticed that online advertisers like Google tend to display ads of lower-pay jobs to women users compared to men. Likewise, doing a search with a name that sounds African American may produce and ad for a tool for accessing criminal records which is less likely to happen otherwise.

#### Social networks

Since social networks are basing content recommendations essentially on other users' clicks, they can easily lead to magnifying existing biases even if they are very minor to start with. For example, it was observed that when searching for professionals with female first names, LinkedIn would ask the user whether they actually meant a similar male name: searching for Andrea would result in the system asking "did you mean ANdrew?" If people occasionally click Andrew's profile, perhaps just out of curiosity, the system will boost Andrew even more in subsequent searches.

There are numerous other examples we could mention, and you have probably seen news stories about them. The main difficulty in the use of AI machine learning instead of rule-based systems is their lack of transparency. Partially this is a consequence of the algorithms and the data being trade secretss that the companies are unlikely to open up for public scrutiny. And even if they did this, it may often be hard to identify the part of the algorithm or the elements of the data lead to discriminating decisions.

><h4>Transparency through regulation?</h4>
>
>A major step towards transparency is the European General Data Protection Regulation (GDPR). It requieres that all companies that either reside within the European Union or that have European customers must:
>
>- Upon request, reveal what data they have collected about any individual (right of access)
>- Delete any such data that is not requiere to keep with other obligations when requested to do so (right to be forgotten)
>- Provide an explanation of the data processing carried out on the customer's data (right to explanation)

The last point means, in other words, that companies such as Facebook and Google, at least when providing services to European users, must explain their algorithmic decision making processes. It is, however, still unclear what exactly counts as an explanation. Does for example a decision reached by using the nearest neighbor classifier (Chapter 4) count as an explainable decision, or would the coefficients of a logistic regression classifier be better? How about deep neural networks that easily involve millions of parameters trained using terabytes of data? The discussion about the technical implementation about the explainability of decisions based on machine learning is currently intensive. In any case, the GDPR has potential to improve the transparency of AI technologies.

![](images/15_2.svg)

### Implication02: Seeing is believing - or is it?

We are used to believing what we see. When we see a leader on the TV stating that their country will engage in a trader-war with another country, or when a well-known company spokesperson announces an important business decision, we tend to trust them better than just reading about the statement second-hand from the news written by someone else.

Similarly, when we see photo evidence from a crime scene or from a demonstration of a new tech gadget, we put more weight on the evidence than on written report explaining how things look.

Of course, we are aware of the possibility of fabricating fake evidence. People can be put in places they never visited, with people they never met, by photoshopping. It is also possible to change the way things look by simply adjusting lightning or pulling one's stomach in in cheap before - after shots advertising the latest diet pill.

><h4>AI is taking the possibilities of fabircating evidence to a whole new level:</h4>
>
>[Face2Face](https://www.youtube.com/watch?v=ohmajJTcpNk) is a system capable of identifying the facial expressions of a person and putting them on another person's face in a Youtube video. 
>
>[Lyrebird](https://www.descript.com/lyrebird-ai?source=lyrebird) is a tool for automatic imitation of a person's voice from a few minutes of sample recording. While the generated audio still has a notable robotic tone, it makes a pretty good impression.

![](images/15_3.svg)

### Implication03: Changing notions of privacy

It has been long known that technology companies collect a lot of information about their users. Earlier it was mainly grocery stores and other retailers that collected buying data by giving their customers loyalty cards that enable the store to associate pruchases to individual customers.

><h4>Unprecedented data accuracy</h4>
>
>The accuracy of the data that tech companies such as Facebook, Google, Amazon and many others is way beyond the purchase data collected by conventional stores: in principle, it is possible to record every click, every page scroll, and the time you spend viewing any content. Websites can even access your browsing history, so that useless you use the incognito mode (or the like) after browsing for flights to Barcelona on one site, you will likely get advertisements for hotels in Barcelona.

However, as such the above kind of data logging is not yet AI. The use of AI leads new kinds of threats to our privacy, which may be harder to avoid even if you are careful about revealing your identity.

#### Using data analysis to identify individuals

A good example of a hard-to-avoid issue is **de-anonymization**, breaking the anonymity of data that we may have thought to be safe. THe basic problem is that when we report the results of an analysis, the results may be so specific that they make it possible to learn something about individiaul users whose data is included in the analysis. A classic examle is asking for the average salary of people born in the given yaear and having a specific zip code. In many cases, this could be a very small group of people, often only one person, so you'd be potentially giving data about a single person's salary.

An interesting example of [a more subtle issue](https://www.wired.com/2007/12/why-anonymous-data-sometimes-isnt/) was pointed out by researchers at the University of Texas Austin. They studied a public dataset made available by Tetflix containing 10 million movie ratings by some 500,000 anonymous users, and showed that many of the Netflix users can actually be linked to user accounts on the Internet Movie Database because they had rated several movies on both applucations. Thus the researchers were able to de-anonymize the Netflx data. While you may not think it's big deal whether someone else knows how you rated the latest *Star Wars* movie, some movies may reveal aspects of our lives (such as politics or sexuality) which we should be entitled to keep private.

#### Other methods of identification

A similar approach could in principle be used to match user accounts in almost any servie that collects detailed data about user bevaviors. Another example is typing patterns. Researchers at the University of Helsinki have demonstrated that users can be identified based on their typing patterns: the short intervals between specific keystrokes when tryping text. This can mean that if someone has access to data on your typing pattern (maybe you have used their website and redistered by entering your name), they can identify you the next time you use their service even if you'd refuse to identify yourself explicitly. They can also sell this information to whoever wants to buy it.

While many of the above examples have come as at least in part as surprises - otherwise they could have been avoided - there is a lot of ongoing resarch trying to address them. In particular, an area called differential privacy aims to develop machine learning algorithms that can guarantee that the results are sufficiently coarse to prevent reverse engineering specific data points that went into them.

![](images/15_4.svg)

### Implication04: Changing work

When an early human learned to use a sharp rock to crack open bonus of dead animals to access a new source of nutrition, tiem and anergy was released for other purposes such as fighting, finding a mate, and making more invitations. THe invention of the steam engine in the 1700s tapped into an easily portable form of machine power that greatly improved the efficiency of factories as well as ships and trains. Automation has always been a path to efficiency: getting more with less. Especially since the mid 20th century, technological development has led to a period of unprecedented progress in automation. AI is a ciontinuation of this progress.

Each step towards better automation changes the working life. With a sharp rock, there was less need for hunting and gathering food; with the steam engine, there was less need for horses and horsemen; with the computer, there is less need for typists, manual accounting and many other data processing (and apparently more need for watching cat videos). With AI and robotics, there is even less need for many kinds of dull, repetitive work.

><h4>A history of finding new things to do</h4>
>
>In the past, every time one kind of work has been automated, people have found new kinds to replace it. The new kinds of wrok are less repetitive and routine, and more varaible and creative. The issue with the current rate of advance of AI and other technologies is that during the career of an individual, the change in the working life might be greater than even before. It is conceivable that some jobs such as driving a truck or a taxi, may disappear within a few years' time span. Such an abrupt change could lead to mass unemploument as people don't have time to train themselves for other kinds of work.
>
>The most important preventive action to avoid huge societal issues such as this is to help young people obtain a wide-ranging education. This that provides a basis for pursuing many different jobs and which isn't high risk of becoming obsolete in the near future.
>
>It is equally important to support life-long learning and learning at work, because there are going to be few of us who will do the same job throughout their entire career. Cutting the hours per week would hep offer work for more people, but hte laws of economics tend to push people to work more rather than less unless public policy regulating the amount of work is introduced.

Because we can't predict the future of AI, predicting the rate and extent of this development is extremely hard. THere have been some estimates about the extent of job automation, raging up to [47% of US jobs being at risk](https://www.economist.com/graphic-detail/2018/04/24/a-study-finds-nearly-half-of-jobs-are-vulnerable-to-automation) reported by researchers at the University of Osford. The extract numbers such as there - 47%, not 45% or 49% -, the complicated-sounding study designs used to get them, and the top universities that report them tend to make the estimates sound very reliable and precise (recall the point about estimating life expectancy using a linear model based on a limited amount of data). The illusion of accuracy to one percentage is a fallacy. The above number, for example, is based on looking at a large number of job descriptions - perhaps licking the tip of your finger and putting it up to feel the wind - and using subjective grounds to decide which tasks are likely to be automated. It is understandable that people don't take the trouble to read a 79 page report that includes statements such as "the task model assumes of tractability an aggregate, constant-return to-scale, Cobb-Douglas production function." However, if you don't, then you should remain somewhat sceptical about the conclusions too. The ral value in this kind of analysus is that it suggests which kinds of jobs are more likely to be at risk, not int the actual numbers such as 47%. The tragedy is that the headlines reporting "nearly half of US jobs at risk of computerization" are noted, and the rest is not.

So then, what actually are the tasks that are more likely ot be automated? There are some clear signs concerning this that we can already observe:

- Autonomours robotics solutions such as self-driving vehicles, including cars, drones and boats or [ferries](https://www.reaktor.com/work/autonomousferry/), are just at the verge of major commercial applications. The safety of autonomous cars is hard to estimate, but hte stadistics suggests that it is probably not yet wuite at the required level (the level of an average human driver). However, the progress has been incredibly fast and it is accelerating due to the increasing amount of available data.

- Customer-service applications such as helpdesks can be automated in a very cost-effective fashion. Currently the quality of services is not always to be cheered, the bottle-necks being language processing (the system not being able to recogniza spoken language or to parse the grammar) and the logic and reasoning required to provide the actual service. However, working applications in constrained domains (such as [making restaurant or haircut reservations](https://www.youtube.com/watch?v=BRUvbiWLwFI)) sprout constantly.

For one thing, it is hard to tell how soon we'll have safe and reliable self-driving cars and other solutions that can replace human work. In addition to this, we mustn't forget that a truck or taxi driver doesn't only turn a wheel: they are also responsible for making sure the vehicle operates correctly, they handle the goods and negotiate with customers, they guarantee the safety of their cargo and passengers, and take care og a multitude of other tasks that may be much harder to automate than the actual driving.

As with earlier technological advances, there will also be new work that is created because of AI. It is likely that in the future, a larger graction of the workforce will focus on research and development, and tasks that require creativity and human-to-human interaction. If you'd like to read more on this topic, see for example Abhian Suri's nice essay on [Artificail Intelligence and the Rise of Economic Inequality](https://towardsdatascience.com/artificial-intelligence-and-the-rise-of-economic-inequality-b9d81be58bec).

### exercise 24: the implications of AI

What kind of articles (in newspapers and magazines or other popular science outlers such as blogs, ...) are being written about AI - and do you think they are realistic? Do an online search about AI related to one of your inteserst. **Choose one of the articles and analyze it.**

1. Mention the **title of the article** along with its author and where it was publisehd (as a URL if applicable) in your answer.

2. Explain the central idea in the article **in your own words** using about a paragraph of text (multiple sentences).

3. Based on your understanding, how accurate are the AI-related statements in the article? **Explain your answer**. Are the implications (if any) realistic? **Explain why or whay not**.

    >Crochet enthusiasts asked ChatGPT for patterns. The results are ‘cursed’
    https://www.theguardian.com/technology/2023/feb/26/chatgpt-generated-crochet-pattern-results
    >
    >The article discusses how crochet enthusiasts have turned to ChatGPT, an artificial intelligence chatbot, to generate crochet patterns. However, the results have been described as "cursed" and unconventional. TikTok users, have experimented with ChatGPT's pattern-making abilities, creating stuffed animals with varying levels of success. While the language-learning tool managed to generate comprehensive instructions resembling crochet patterns, the final products were described as strange and oddly adorable. Crochet patterns pose challenges for AI due to their reliance on numbers and intricate stitching techniques. 
    Although ChatGPT excels in creativity, it struggles with context and understanding the meaning behind words and numbers - in crochet this is vital, because each one of the symbols represents something in reality, but ChatGPT doesn't have the ability yet to understand the outcome.
    > 
    >Despite its shortcomings, the collaboration between humans and AI in the realm of crochet is seen as an intriguing exploration of the boundaries of artificial intelligence.

## III. Summary

<h3>The most important decisions that determine how well our society can adapt to the changes brought by AI aren't technological. They are political.</h3>

Everythin that we have learned about AI suggests that the future is bright. We will get new and better services and increased productivity will lead to positive overall outcomes - but only on the condition that we carefully consider the societal implications and ensure that the power of AI is used for the common good.

### What we need to do to ensure a positive outcome

Still we have a lot of work to do.

- We need to avoid algorithmic bias to be able to reduce discrimination instrad of increasing it.

- We also need to learn to be critical about what we see, as seeing is no longer the same as believing - and develop AI methods that help us detect fraud rather than just making it easier to fabricate more real-looking falsehoods.

- We need to set up regulation to guarantee that people have the right to privacy, and that any violations of this are strictly penalized.

We also need to find new ways to share the benefits to everyone, instead of creating an AI elite, those who can afford the latest AI technology and use it it access unprecedented economic inequality. This requires careful judgement (note that by political judgement, we mean decisions about policy, which has little to do with who votes for whom in an election or the comings and goings of individual politicians and political parties).

><h3>The importance of policy</h3>
>
>The most important decisions that determine how well our society can adapt to the evolution of work and to the changes brought by AI aren't technological. They are political. 
>
>The regulation of the use of AI must follow democratic principles, and everyone must have an equal say about what kind of a society we want to live in in the future. The only way to make this possible is to make knowledge about technology freely available to all. Obviously, there will always be experts in any given topic, who know more about in than the rest of us, but we should at least have the possibility to critically evaluate what they are saying. 

What you have learned supports this goal by providing you the basic background about AI so that we can have a rational discussion about AI and its implications.

### Our role as individuals

As you recall, we started this course by motivating the study of AI by discussing prominent AI applications that affect all our lives. We highlighted three examples: self-driving cars, recommendation systems, and image and video processing. During the course, we have also discussed a wide range of other applications that contribute to the current technological transition.

><h3>Hidden agenda</h3>
>
>We also had a hidden agenda. We wanted to give you an opportunity to experience the thrill of learnig, and the joy of eureka moments when something that may have been complicated and mysterious, becomes simple and if not self-evident, at least comprehensible. These are moments when our curiosity is satisfied. But such satisfication is temporary. Soon after we have found the answer to one question, we will ask the newxt. What then? And then?
>
>If we have been succesful, we have whetted your appetite for learning. We hope you will continue your learning by finding other courses and further information about AI, as well as other topics of your interest. To help you with your exploration, we have collected some pointers to AI material that we have found useful and interesting.

Now you are in a position where you can find out about what is going on in AI, and what is being done to ensure its proper use. You should do so, and whenever you feel like there are risks we should discuss, or opportunities we should fo after, don't wait that someone else reacts.

### exercise25: AI in your life

How do you see AI affecting you in the future, both at work and in every day life? Include both the positive and possible negative implications.

    AI is a tool, so by itself it doesn't have any implications. The thing is how you use AI in day-to-life, that can generate positive or negative implications. I will list some examples of both:

    Positive implications of AI:

    - Efficiency: AI has the potential to automate repetitive tasks and enhance productivity in various industries, freeing up time for humans to focus on more creative and complex tasks. Also, AI can learn from your behaviors and patterns and "learn" how to improve the repetitive process.

    - Accuracy: AI algorithms can analyze vast amounts of data quickly and accurately, leading to more precise decision-making and outcomes in fields like healthcare, finance, and scientific research. It sometimes can be more accurate than humans - as we sometimes are tired or don't recognize patterns as easily, helping to make more accurate decisions.

    - Convenience: AI-powered technologies, such as virtual assistants and smart home devices, can simplify daily tasks, provide personalized recommendations, and improve overall convenience in everyday life. In this sense, we currently live with this AI: Spotify, Amazon, Netflix, currently use this systems and we use them in our lives in order to see a movie or to listen to new music or watch a new YouTube video.

    Possible negative implications of AI:

    - Job displacement: The automation of certain tasks by AI could lead to job losses in certain industries, requiring individuals to adapt their skills or seek employment in new areas. As it can happen with the use of AI systems of ChatGPT, this tool can generate information that can eventually replace the work of translators or journalists. 

    - Ethical concerns: AI raises ethical questions regarding privacy, data security, and biases within algorithms, as the people that develop the algorithms come from a very specific background. Ensuring that AI systems are fair, transparent, and respectful of user privacy will be crucial and it depends on the engineers that develop it - we need AI engineers from diverse backgrounds, not only ethnically but also from other disciplines such as philosophers or psychologist. 

    - Overreliance on AI: Excessive dependence on AI systems without critical thinking and human oversight could lead to potential errors or misuse of technology, especially in critical areas like media. Right now an AI can generate images that could be misused and polarised the society.

    It is important to note that the impact of AI will depend on various factors, including how it is developed, regulated, and integrated into different sectors. Balancing the benefits and risks of AI will require responsible development, ongoing research, and proactive policy-making.

### This ia not the end - this is the beginning.

That’s it for now. We thank you for joining us. This has been a great adventure for us, and we really hope that you enjoyed it too. We are not yet finished with the course, and I believe we will never be. We will keep doing our best updating and improving it, and making it the best AI MOOC in the world.

Like the course isn’t finished, you shouldn’t think that your exploration of AI is finished either. The progress is quite rapid and it may seem too much to keep track of, but the comforting news is that the basic principles have stayed more or less the same decade after decade. As long as you know the basics about problem-solving strategies, handling uncertainty, and learning from data, you should be able to easily put new things into perspective. This is why you had to draw diagrams with chickens crossing rivers, Towers of Hanoi, why you had to calculate the probability of rain in Helsinki, or detect happy faces by a neural network. Knowing the fundamentals, or the elements of AI, is much longer lasting knowledge than learning the technical details of a particular AI solution.

Below we give a few pointers that we have found useful. Keep learning, stay curious.

    "The future has not been written. There is no fate but what we make for ourselves." (John Connor)

- The equel to this course, [Building AI](http://buildingai.elementsofai.com/?_ga=2.112874948.1717926132.1685635114-2034105223.1684856055)

- Check out other University of Helsinki's open online courses at [mooc.fi](https://mooc.fi/en).

- See which courses MinnaLearn has to offer [courses.minnalearn.com](https://courses.minnalearn.com/).

- You are welcome to apply to [the University of Helsinki](https://www.helsinki.fi/en/studying) too!

- Looking to train your company in AI? See [Elements of AI for business](https://www.minnalearn.com/elements-of-ai-for-business/).

- Recommended programs for continued education: ['AI Diploma' by HY+/Aalto PRO/FCAI](https://www.aaltopro.fi/aidiploma), and ['AI:n perusteet' by Aalto Executive Education (in Finnish)](https://www.aaltoee.fi/aiperusteet).

- Our advisor, Risto Siilasmaa’s ["What is Machine Learning" video](https://www.youtube.com/watch?v=KNMy7NCQDgk) (1h 18min)

- [A friendly introduction to machine learning](https://www.youtube.com/watch?v=IpGxLWOIZy4) (Luis Serrano/Udacity) (30min)

- Andrew Ng’s [Machine Learning MOOC](https://www.coursera.org/learn/machine-learning) at Coursera

- Udacity [School of AI](https://eu.udacity.com/school-of-ai)

- Machine Learning - [Learn AI with an AI (Korbit)](https://korbit.ai/machinelearning)

## Recap

- Understanding the difficulty in predicting the future and be able to better evaluate the claims made about AI.

- Indentify some of the major societal implications of AI including algorithm bias, AI-generated content, privacy, and work.