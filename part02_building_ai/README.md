# Table of contents
## [chapter01: getting started with ai](#chapter01-getting-started-with-ai)

[I. why ai matters](#i-why-ai-matters)
<br>[II. optimization](#ii-optimization)
<br>[III. hill climbing](#iii-hill-climbing)

## [chapter02: dealing with uncertainty](#chapter02-dealing-with-uncertainty)

[I. probability fundamentals](#i-probability-fundamentals)
<br>[II. the Bayes Rule](#ii-the-bayes-rule)
<br>[III. Naive Bayes classifer](#iii-naive-bayes-classifier)

## [chapter03: machine learning](#chapter03-machine-learning)

[I. odds and probability](#i-linear-regression)
<br>[II. the bayes rule](#ii-the-nearest-neighbor-method)
<br>[III. naive bayes rule](#iii-working-with-text)
<br>[IV. overfitting](#iv-overfitting)

## [chapter04: neural networks](#chapter04-neural-networks)

[I. Logistic Regression](#i-logistic-regression)
<br>[II. From Logistic Regression to Neural Networks](#ii-from-logistic-regression-to-neural-networks)
<br>[III. Deep Learning](#iii-deep-learning)

## [chapter05: conclusions](#chapter05-conclusions)

[I. summary](#i-summary)
<br>[II. Your AI idea](#ii-your-ai-idea)
<br>[III. AI idea gallery](#iii-ai-idea-gallery)


# Chapter01: Getting started with AI

## I. Why AI matters

<h3>In this course, we're going to take you on a journey towards your first implementable AI idea and give you the tools to make it a reality. The path begins by looking into the algorithms that make artificial intelligence methods possible. But before we start, we wanted to take a brief moment to discuss why AI matters in the first place.</h3>

In a word, relevance. Artificial intelligence, or at leas "narrow AI" (AI that handles only one task), is already a part of our dailly lives. When we search online, use our smartphone to take and edit a picture, ask Siri or Alexa for a recommendation, or use GPS navigation, we're relying on AI methods. In practice this means we're already surrounded by AI, and this influence only looks set to grow.

As you will find in this course, we think this influence is a good thing - so lon as we're smart about it. After all, AI is simply a collection of methods for solving problems. We think that AI is too important to leace just to tech experts. That's why our goal is to empower as many people as possible to be part og creating meaningful AI solutions to real-world problems. Building AI is for anyone who wants to improve their AI-related vocabulary and skills, including non-programmers and people who can program in Python. By taking the course, you'll learn more about what makes different AI methods possible and where and how these methods can be applied in real life - helping you to communicate about AI and take part in AI-related projects. 

For some of you, this course will also be the first step towards actually being able to program these methods. From here, you'll be able to go to more advanced courses that really delve into the programming. By finishing this course, you'll be able to start firmulating a realistic, useful and implementable AI idea - which can become your own project that you develop as far as you want.

### What AI looks like in real life

Here are just a few examples of where you can find AI methods at work. These are all real-life cases that we will look at in more detail in later chapters:

|   |   |
| - | - |
| ![](images/1_1.svg) | **<h4>Content recommendation</h4>** All of us are familiar with content recommendation systems (think Netflix or YouTube). But as it turns out, commonly used recommendation algorithms are good for example at recommending popular shows (like drama) while downplaying other areas like educational or scientific content. But this can be changed, increading people's exposure to broader types content. |
| ![](images/1_2.svg)  | **<h4>Online shopping</h4>**  So much choice, so little time. But how do you make browsing tens of thousands of items convenient, expecially on a mobile phone? Machine learning methods can recommend products based on the purchase behavior of an individual user as well as other customers who purchased similar products.|
| ![](images/1_3.svg)  | **<h4>Online support</h4>** Nearly half of social media users have encountered online bullying or harassment online. Machine learning methods based on Natural Language Processing (NLP) can be used to provide scalable legal and psychological first aid online |
| ![](images/1_4.svg) | **<h4>Resources mapping</h4>** What kind of critical infraestructure (like schools) exists in your country? In a lot of places around the world, the answer is "not sure". But having an accurate and comprehensive map of infraestructure is a key tool for measuring and improving quality. Heuran networks can be trained to identify features from looking at high-resolution satellite images in order to identify buildings and create accurate maps.  |
| ![](images/1_5.svg) | **<h4>Waste sorting</h4>** Reduce, reuse, recycle - we're all familiar with the mantra, and most of us dutifully sort our waste. But what happens after that? The fact is a lot of what we "recycle" still ends up in a landfill or is incinerated. But using neural networks can enable robots to sort waste and improve recycling rates. |
| ![](images/1_6.svg) | **<h4>Your AI idea</h4>** For learning purposes, this is probably the most important example of real-life AI in this course, simply because it's yours. The optional project in Chapter 5 is the endpoint of your Elements of AI journey and the final stepping stone after which you'll be able to present your idea to the wider AI community. |

><h3>Working with AI in real life</h3>
>
>People can encounter and use AI in their work in many different ways. Here are three common examples:
>
>- You can work as a professiona who has a good understanding of AI methods and the ability to ideate realistic solutions that involve an AI component. The ability to combine an understanding of AI with knowledge from other fields can lead to valuable results, even if you're not writing the code yourself.
>
>- Those who are more interested in the infrastructure behind what makes AI systems tick can work, for instance, as Data Engineers. A Data Engineer makes sure that data flows where it is neede and is of the right type and quality for specific AI solutions. It's crucial with real-life, large-scale, production-ready AI systems to get the supporting infrastructure right so as to avoid the so called "garbage in, garbage out" problem
>
>- THose who have a dep understanding of AI algorithms can apply this methods to real-life problems with job titles such as AI Developer, AI Engineer, or Data Scientist. To excel in this area, you need to have rpoven track record in applyting AI to defferent types of problems. In addition to the technical skills, you should apply AI in the first place, and when not.
>
>The world seems to be full of people who claim to be AI evangelists but what modern companies are looking for is people who can make things happen and who actually understand what AI is and what it isn't capable of - and that's exactly whar this courtse can help with. [Read Mikko's career story as an example here](https://www.reaktor.com/blog/a-letter-from-your-future-colleague-mikko/)
>
>If you are aiming fot a career in Data Science, you may wish to consider in applying, for instance, to the [University of Helsinki's Master Programme in Data Science](https://www.helsinki.fi/en/admissions/degree-programmes/data-science-masters-programme)

### How this course takes you towards real-life AI solutions

It takes a lot of steps to get to the level where you can actually create AI methods. This courtse exists to help bridge the gap between a total beginner course in AI (like the [Elements of AI: Introduction to AI](https://course.elementsofai.com/)) and more advanced machine learning / AI courses available now.

One of our goals with this course is also to help introduce you to the broader AI community. For the reason, Chapter 5 is an optional project suitable for all the students taking this course, whatever the level. With our final project, we want to encourage you to step out of this sandbox and get your hands dirty with some "reall world" AI programming (even if it's simple) and we'll introduce you to GitHub, the leading code sharing platform where everyone in the AI community comes together to collaborate.

For those of you who don't program, you can still take part by following the template of questions in Chapter 5 to begin outlining a problem that could be potentially solved by AI, and the kind of methods that might work to solve it. We ultimately hope you can share your ideas in your workplace or connect with potential developers and see your idea come to life. We'll also offer a chance to showcase ideas and the projects that grow out of this course in our GitHub gallery.

You'll get the necessary tools to prepare you for submitting and idea by completing this course and the accompanying exercises

## II. Optimization

<h3>You may ask "what do we mean when we talk about AI? Is it something very advanced like deep neural netwotks and complex algorithms, or is it just a fancy word for any software?</h3>

Unfortunately, we can't give a precise definition. WHy? Because there isn't one. THe field of AI doesn't have a commonly agreed definition (we discuss this topic in some detail on [Chapter 1](https://course.elementsofai.com/1/1) of the Introduction to AI course). We argue that it's often the way the technology is being used, rather than the technology itself, that determines whether it is appropriate to call it AI or not.

><h3>A case in point: optimization</h3>
>
>A good example of something that can be AI or not, depending on the use case, is optimization. As you will see, some optimication. As you will see, some optimization algorithms are very, very simple, and can be implemented in a few lines of code. However, we will argue that the outcome may be considered intelligent behavior, which many of us would call AI without qualms.

In an [Introduction to AI](https://course.elementsofai.com/2) (Chapter 2), we showed how various "brain teasers" or puzzles, like the towers of Hanoi or the Chicken Crossing Puzzle, can be formulated as search problems and solved in a straightforward manner by finding a path from the starting point to the goal.

When we have the superpower for programming, we can scale this up to much bigger problems than before when we have to solve everything with a pencil and paper. We will start with an absolute classic, the so-called Traveling Salesperson Problem (or TSP, for those who love [TLAs](https://en.wikipedia.org/wiki/Three-letter_acronym))

><h3>An example optimization task</h3>
>
>Imagine that you've been assigned the task to plan the route of a container ship loaded with pineapples. The ship starts in Panama, loaded with delicious Fairtrade pineapples. THere are four other ports, New York, Casablanca, Amsterdam, and Helsinki, where pineapple-craving citizens are eagerly wating. The ship must visit wach of the four destination ports exactly once, but the order in which wach part is visited is free. The goal is to minimize the carbon emissions, which means that a shorter route is better than a longer one.

![](images/2_1.svg)

To solve this problem, it is wnoguh to list all the possible routes that start from Panama and visit wach other ports wxactly once, calculate the carbon emissions of each route, and printo ut the one with the least emissions.

Let's consinder each stage separately, starting from listing all the possible alternatives. The term used by programmers is enumerate. So we'll first **enumerate** all the possible routes. THose of you who are well-versed in combinatorics (the part of mathematics that deals with combinations of finite sets of objects) will know that the number of routes is `4 * 3 * 2 * 1 = 24`. 

### exercise01: listing pineapple routes

How many routes would there be if all the people in Helsinki were allergic to pineapple? In other words, what is the number of routes from a given starting point to three other ports (instead of four)? 

6 -> Correct. The formula for counting the number of routes is 1 x 2 x 3 x ... where the last number is the number of ports, not including the starting points. So if there are three other ports, the number is 1 x 2 x 3 = 6.

### What this teaches us

Just listing the alternatives is not very useful byt at least it helps us realize that the number of routes starting to be so high that finding the best one manually would be a chore. There are 24 routes for five ports (one of which is the starting point). If some pineapples were also wanted in, say, London, if could be added in the route in five different positions so the number would become `5 * 24 = 120`. With yet another destination, whis number would be multiplied by 6, to get `6 * 120 = 720`.

>The formula `1 * 2 * 3 * ... * n` is called a *factorial* and it gores **really** fast. For 10 destinations (in addition to the starting point in Panama), the number of routes is already 3,628,800. This means that very quickly a manual solution is completely out of the question.

An automatic solution using a computer can take us much further. However, without some clever strategies to reduce the workload, eeven a computer will choke sooner or later. Which is where more advanced AI techniques step in. But let's not rush ahead of ourselves before we have to - let's work out our route to get the pineapples delivered to the four cities with minimal carbon emissions.

Having listed the alternatives, next we can calculate the carbon emissions for each of them. Below you will find the distances between portis in kilometers in a five-by-five table.

|	 |PAN | AMS| CAS | NY | HEL |
| - | - | - | - | - | - |
| PAN | 0| 8943 | 8019 | 3652 | 10545 | 
| AMS |8943 | 0 | 2619 | 6317 | 2078 |
| CAS | 8019 | 2619 | 0 | 5836 | 4939 |
| NY | 3652 | 6317 | 5836 | 0 | 7825 |
| HEL | 10545 | 2078 | 4939 | 7825 | 0 |

Let's assume that the boat is realtively modern and produces 0.020 kg of CO2 emissions per kilometer for the amount of pineapples that we are shippong. Thus, you can calculate the emissions caused by traveling from Panama to Amsterdam by first looking up the distance in the first row, second column of the table (highlighted in the above table): 8943 km, and then multiplying this with 0.020kg/km to get 178.9 kg.

### ecercise02: pineapple route emissions

Using the reference table, calculate the emissions produced by the following three routes. Which produces the least emissions?

- PAN, AMS, CAS, NY, HEL -> 623.18

- PAN, NY, CAS, AMS, HEL -> 283.7 -> less emisions

- PAN, NY, AMS, CAS, HEL -> 350.7

correct! The total distances are 25,223.0 km, 14,185.0 km, and 17,527.0 km. The corresponding emissions are 504.5 kg, 283.7 kg, and 350.5 kg, respectively. So the second route is the shortest and produces the least emissions. If you look at the map, the second route makes sense since it starts from Central America, stops at North America, crosses the Atlantic to stop at the African continent before continuing to Central Europe and finally to Northern Europe.

## III. Hill climbing

# Chapter02: Dealing with uncertainty

## I. Probability fundamentals

## II. The Bayes Rule

## III. Naive Bayes classifier

# Chapter03: Machine Learning

## I. Linear Regression

## II. The nearest neighbor method

## III. Working with text

## IV. Overfitting

# Chapter04: Neural networks

## I. Logistic regression

## II. From logistic regression to neural networks

## III. Deep Learning

# Chapter05: Conclusions

## I. Summary

## II. Your AI Idea

## III. AI idea gallery