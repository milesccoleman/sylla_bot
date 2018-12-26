[home](https://milesccoleman.com)

#### [Live Example](https://digitalrhetoric-syllabot.herokuapp.com) 

<iframe src="https://digitalrhetoric-syllabot.herokuapp.com" height="250px" width="100%"></iframe>

This is a machine-learning assisted chatbot designed to learn your syllabus and be able to answer questions from it. 

Sylla_bot is built from chamkank's [Flask Implementation](https://github.com/chamkank/flask-chatterbot) of [ChatterBot](https://github.com/gunthercox/ChatterBot). 

# Quick Start
Setting up sylla_bot is relatively simple. Even if you don't program, you will be able to follow the steps below to get your own syllabus into a working chatbot. 

_Note: These instructions are written for people who do not program. If you already use the Git CLI, keep this in mind._  

## Things You Will Need Before Starting
1. Your syllabus, ideally broken up with descriptive headings and saved as a `.txt` file. 
2. A [GitHub](https://github.com) account. 
3. A [Heroku](https://heroku.com) account.
4. A text editor, such as [BBEdit](https://www.barebones.com/products/bbedit/). 

## Formatting the Syllabus
This might sound redundant, especially if you're like me and spend hours putting in headings and lists to make your syllabi readable. But, because we'll be rendering our syllabus into little chunks to be repeated by the bot, we'll need to help the bot do its job. 

### Making the Syllabus Bot-Readable
First, you'll need to "chunk" your syllabus content onto complementary lines. The way the software will read your syllabus is based on associated sequences of characters compared across lines as they are listed in the text file. 

So, if I have a `.txt` file of my syllabus, and in that file I have the instructor's name, and I want to make that accessible when someone eventually asked the bot who teaches the course, I would put the following in my text file. 

```
Who instructor professor teacher teaches  
Dr. Miles Coleman
```

Notice that the user's question is listed first, with the answer content listed second. This will be the format of your entire file. Also, you will see that I am only including a minimized version of the question the machine would need in order to retrieve the information chunk the user is asking for (which included variations of verbs and nouns--e.g., teacher and teaches). This will make it less likely to confuse the bot. Be direct and descriptive, focus on the "meat" of your inquiries. 

### Formatting for Human Eyes
Let's say I also have information about my course schedule, including readings and assignments. Because the `.txt` file will eventually be interpreted as HTML, I can use `<br>`s to format my contents with paragraph breaks. This is super helpful as much of this content can be fairly muddy to read without that formatting. Here's an example. 

```
Week 1 January 7
Topic: <br>Defining Digital Rhetoric (F2F)<br><br>Readings: <br>Hahn, L. K. & Paynton, S. T. . Rhetorical criticism. In Survey of Communication Study. <br>Deuze, M. (2006). Participation, remediation, bricolage: Considering principal components of a digital culture. The information society, 22(2), 63-75. <br>Hess, A. (2018 . Introduction: Theorizing digital rhetoric. In Theorizing Digital Rhetoric. <br><br>Assignments: <br>Community Activity 1 <br>Student Survey <br>Reading Quiz 1. 
```

Because I want students to be able to ask what is due on a given week, as well as to be able to ask for a specific week of the term, I have included both of those nouns (i.e., "Week 1" and "Janurary 7") in the inquiry line.

Each of the `<br>`s helps to format my blob of content from the information chunk I've included. 

Rendered in HTML, that content would be: 

> Topic: <br>Defining Digital Rhetoric (F2F)<br><br>Readings: <br>Hahn, L. K. & Paynton, S. T. . Rhetorical criticism. In Survey of Communication Study. <br>Deuze, M. (2006). Participation, remediation, bricolage: Considering principal components of a digital culture. The information society, 22(2), 63-75. <br>Hess, A. (2018 . Introduction: Theorizing digital rhetoric. In Theorizing Digital Rhetoric. <br><br>Assignments: <br>Community Activity 1 <br>Student Survey <br>Reading Quiz 1. 

Between each question/answer information chunk, I include a space to help read the content easier. 

For example: 

```
Week 1 January 7
Topic: <br>Defining Digital Rhetoric (F2F)<br><br>Readings: <br>Hahn, L. K. & Paynton, S. T. . Rhetorical criticism. In Survey of Communication Study. <br>Deuze, M. (2006). Participation, remediation, bricolage: Considering principal components of a digital culture. The information society, 22(2), 63-75. <br>Hess, A. (2018 . Introduction: Theorizing digital rhetoric. In Theorizing Digital Rhetoric. <br><br>Assignments: <br>Community Activity 1 <br>Student Survey <br>Reading Quiz 1. 

Week 2 January 14
Topic: <br>Asking Questions about Digital Rhetoric (At Home)<br><br>Readings: <br>Gunkel, D. (2018). Critique of digital reason. In Theorizing Digital Rhetoric. <br>Ceccarelli, L. The Ends of Rhetoric: Aesthetic, Political, Epistemic. In Making and Unmaking the Prospects for Rhetoric. Lawrence Erlbaum Associates, 65-73. <br>Eyman, D. (2015). Defining and locating digital rhetoric. In Digital Rhetoric: Theory, Method, Practice. University of Michigan Press, 12-60. <br><br>Assignments: <br>Science, Art, or Politics Survey <br>Set up Issue Crawler and Google <br>Post Draft of Artifact Proposal <br>Reading Quiz 2
```
Find a complete example of a syllabus `.txt` file at the bottom of this page. 

## Getting Code from GitHub and Training the Bot 

### Part I
1. Sign into your GitHub account
2. Go to [this](https://github.com/milesccoleman/sylla_bot) repository
3. Click "Fork"
4. Go to your repositories list, find the sylla_bot repository
5. Click "Download Zip"
6. Unzip the file so that it is on the desktop
7. Delete the file `db.sqlite3`
8. Open the file `chats.txt` in a text editor 
9. Replace the text in that file with your pre-formatted syllabus content and save it 
10. Open `app.py`
11. On line 9 of `app.py` replace `True` to `False` within `read_only=True,` and save it

### Part II
1. Find the "Terminal application on your computer 
2. Open Terminal and enter the following commands, one at a time 
3. After your software is done downloading, enter the following command
```
python app.py
```
4. After the bot is done training, go back to `app.py`
5. On line 9 of `app.py` put `False` back to `True` within `read_only=False,` and save it

## Putting the Bot Code back no GitHub
1. Go back to your sylla_bot repository on GitHub
2. Click on `db.sqlite3`
3. Delete `db.sqlite3`
4. Click on `chats.txt`
5. Delete `chats.txt`
6. Click on `app.py`
7. Delete `app.py`
8. From the folder on your desktop, drag and drop your own `db.sqlite3`, `chats.txt`, and `app.py` files
9. "Commit" the additions of these files
10. Click "Clone or download" 
11. Copy the clone URL, you'll need it for our next step

## Deploying to Heroku

### Part I
1. Open your Heroku dashboard
2. Click "New" --> "Create new app"
3. Name your app anything you want. I've chosen "syllabusbot" 
4. Choose your appropriate region. I've chosen "United States"
5. Click "Create App" 
6. Click on "Settings" 
7. Click "Add buildpack" 
8. Click "Python" 
9. Go to the "Deploy" tab
10. Under "Deployment method," click "GitHub"
11. Put in your GitHub account details for your sylla_bot repository
12. Click "Connect" 
13. Click "Deploy branch" 
14. Your bot should install and deploy automatically
15. "View" the bot, and copy the URL--you now have your very own syllabus chatbot

## Example Syllabus Formatting

```
What name title called course
Foundations of Digital Rhetoric

Who instructor professor teacher teaches  
Dr. Miles Coleman

Email
colemanm@seattleu.edu

What describe tell me what is digital rhetoric <br>
Digital rhetoric is the study of how digital technologies shape methods of persuasion. <br>You’ll analyze the obvious and hidden values and arguments that exist in things like video games, search engines, webpage designs, digital networks, and digital images. 

Why study digital rhetoric what does digital rhetoric offer
Effective communication relies on the artistic abilities of individuals to inform and persuade others. <br>The growing body of knowledge and tools used to understand that art is called rhetoric. Rhetorical criticism is the act of putting that mass of knowledge to work to help us more critically assess the communication we consume, as well as the communication we produce. In our so-called, “information age,” we use media that have within them embedded arguments, implicitly and explicitly persuading us to think, do, and believe in certain ways. The job of the (digital) rhetorical critic then, is to study, analyze, and evaluate the communicative practices and technologies that exist in our publics so that persons can communicate more effectively and more thoroughly appreciate the communication of others. This course is important because someone who knows how to do good rhetorical criticism of digital phenomena is likely also someone apt to understand what it means to communicate well in an era permeated by digital technologies.

Assignments coursework
Together, the course assignments equal 940 pts total, consisting of: <br>Participation (100 pts) <br>7 Community Assignments (70 pts) <br>8 quizzes (200 pts) <br>3 practice analyses (150 pts) <br>1 artifact proposal (35 pts) <br>1 artifact description paper (85 pts) <br>1 feedback report (40 pts) <br>1 final paper meeting (10 pts) <br>final project/reflection (250 pts) <br>Ask me about specific assignments to get more detail about each. 

Participation
A portion of your grade consists of participation, both online (e.g., on discussion boards, small online activities, e-mail correspondence) and face-to-face (e.g., in class discussions and activities), and is based on frequency and quality of contributions to class. <br>(You can find the specific items to be calculated into your participation score in the assignments list. [For clarity it's probably best to set the display of the assignments list to "type"].)

Community Assignments
There are eight online community assignments. They take various forms (e.g., discussion board posts, and online “pair shares”). <br>You will create your own post and then comment on at least two other students’ work. <br>These assignments are meant to spark conversation and to capitalize on student experience to enrich course material.

Quizzes
There will be four quizzes based on readings and discussion, given every other week. <br>You will be given reading prompts before the readings are assigned from which the quizzes are written. <br>And, before the quiz, you will be given an opportunity to ask clarifying questions about concepts. <br>The quizzes will be multiple choice and short answer, delivered through the course web page.

Artifact Proposal
In the second week of class you will turn in an artifact proposal. <br>In this 1-2 page document you will briefly describe a digital artifact that you would like to analyze for your class project. <br>This paper should provide a rationale for why it is important that this artifact be analyzed.

Practice Analyses
Throughout the quarter there will be three frames of digital rhetorical analysis introduced. <br>For each of these frames you will write a 1.5-2 page analysis of an artifact of your choosing. <br>These practice analyses are meant to help you build material for your final paper. <br>You can find more info on these assignments by clicking on Practice Analysis 1, Practice Analysis 2, and Practice Analysis 3.

Artifact Description/Background Paper
You will turn in a 3-4 page paper that describes the details and background information necessary for an analysis of your chosen artifact. <br>This paper is meant to help you develop the front half of your final paper.

One-on-One Final Paper Meeting
You will meet with your instructor once at the end of the quarter to discuss your final paper. <br>This meeting will require you to be prepared with specific questions about, and possible solutions to, any "rough spots" in your work.

Feedback Report
You will craft a one-page, single-spaced report evaluating and critiquing the writing and media included in the penultimate draft of a fellow classmates’ final project.

Final Project
Working from the foundation of work you have put into the proposal, the description/ background paper, and the practice analyses, you will write a 5-8 page rhetorical analysis of a digital artifact that includes multimodal elements as appropriate, and includes description, method, analysis, and action sections, eightbibliographic citations and, of course, is abounding with insight about digital communication.

Reflection Paper
Using what you discover in the work you do on your final paper, you will write a 1 page reflection paper that affords you a venue to ruminate on the things you might have discovered you had skills or interest in, and things you would like to continue to work on. The reflection asks that you analyze your work, connecting it to course and program learning outcomes to make an argument about your growth and needs for improvement.

Week 1 January 7
Topic: <br>Defining Digital Rhetoric (F2F)<br><br>Readings: <br>Hahn, L. K. & Paynton, S. T. . Rhetorical criticism. In Survey of Communication Study. <br>Deuze, M. (2006). Participation, remediation, bricolage: Considering principal components of a digital culture. The information society, 22(2), 63-75. <br>Hess, A. (2018 . Introduction: Theorizing digital rhetoric. In Theorizing Digital Rhetoric. <br><br>Assignments: <br>Community Activity 1 <br>Student Survey <br>Reading Quiz 1. 

Week 2 January 14
Topic: <br>Asking Questions about Digital Rhetoric (At Home)<br><br>Readings: <br>Gunkel, D. (2018). Critique of digital reason. In Theorizing Digital Rhetoric. <br>Ceccarelli, L. The Ends of Rhetoric: Aesthetic, Political, Epistemic. In Making and Unmaking the Prospects for Rhetoric. Lawrence Erlbaum Associates, 65-73. <br>Eyman, D. (2015). Defining and locating digital rhetoric. In Digital Rhetoric: Theory, Method, Practice. University of Michigan Press, 12-60. <br><br>Assignments: <br>Science, Art, or Politics Survey <br>Set up Issue Crawler and Google <br>Post Draft of Artifact Proposal <br>Reading Quiz 2

Week 3 January 21
Topic: <br>The (Digital) Public Sphere (F2F) <br><br>Readings: <br>Wise, J. M. (2018 ). Towards a minor assemblage: An introduction to the clickable world. In Theorizing Digital Rhetoric. <br>“The public sphere.” (2015). Wikipedia. <br>“Technology and the Public Sphere.” (2013) Wikibooks. <br>Papacharissi, Z. (2002). The virtual sphere The internet as a public sphere. New Media & Society, 4(1),9-27. <br><br>Assignments: <br>Post Draft of Artifact Description/Background Paper. <br>Launch Issue Crawl <br>Artifact Proposal <br>Quiz 3

Week 4 January 28
Topic: <br>Networked Publics (At Home)<br><br>Readings: <br>Coleman, M. C. (2017). Rhetorical Logic Bombs and Fragmented Online Publics of Vaccine Science. Journal of Contemporary Rhetoric, 7(4), 203-216. <br>Baym, N. & Boyd, D. (2012). Social mediated publicness: An introduction. Journal of Broadcasting and Electronic Media, 56(3), 320-329. <br>Rogers, R., & Marres, N. (2000). Landscaping climate change: A mapping technique for understanding science and technology debates on the World Wide Web. Public Understanding of Science, 9(2), 141-163. <br><br> Assignments: <br>First Try at Practice Analysis 1 <br>Artifact Description/Background Paper <br>Reading Quiz 4

Week 5 February 4
Topic: <br>Materiality and Nonhuman Rhetorics (F2F)<br><br>Readings: <br>Zappen, F. P. (2018). Digital rhetoric and the internet of things. In Theorizing Digital Rhetoric. <br>Coleman, M. C. (2018). Machinic Rhetorics and the Influential Movements of Robots. Review of Communication. <br>Rickert, T. (2013). "The Rhetorical Thing: Objective, Subjective, Ambient." In Ambient Rhetoric. <br><br>Assignments: <br>Practice Analysis 1--Networked Public Analysis <br>Reading Quiz 5 <br>Post Final Project "Rough Plan"

Week 6 February 11
Topic: <br>Algorithms and Software Rhetorics (At Home)<br><br>Readings: <br>Reyman, J. (2018). The rhetorical agency of algorithms. In Theorizing Digital Rhetoric. <br>“What is an algorithm and why should you care?” (2015). Khan Academy. <br>Bogost, (2007); Procedural rhetoric. In Persuasive Games: The Expressive Power of Video Games. <br>Brown, J. J. (2015). Possibility Spaces: Exploits and persuasion. Ethical programs: Hospitality and the rhetorics of software. <br><br>Assignments: <br>Set up Axure and Power Mapper <br>First Try at Practice Analysis 2 <br>Reading Quiz 6

Week 7 February 18
Topic: <br>Visual Rhetoric (F2F)<br><br>Readings: <br>Jones, H. (2018). Pinning, Gazing, and Swiping Together: Identification in Visually Dirven Social Media. In Theorizing Digital Rhetoric. <br>Edwards, J. L. (2009). “Chapter 25: visual rhetoric.” In 21st century communication: A Reference Handbook. Sage Publications, 220-229. <br>Gries, L. E. (2013). Iconographic tracking: A digital research method for visual rhetoric and circulation studies. Computers and Composition, 30(4), 332-348. <br>Harold, C. (2004). Pranking rhetoric: “Culture jamming” as media activism. Critical Studies in Media Communication, 21(3), 189-211. <br><br>Assignments: <br>First Try at Practice Analysis 3 <br>Practice Analysis 2--Procedural Rhetorical Analysis <br>One-on-One Meeting <br>Reading Quiz 7

Week 8 February 25
Topic: <br>Putting Digital Rhetoric to Work (At Home)<br><br>Readings: <br>Pucillo, F., & Cascini, G. (2014) A framework for user experience, needs and affordances. Design Studies, 35(2), 160-179. <br>User Experience Basics. (2018) gov. <br><br>Assignments: <br>Trends Analysis <br>Practice Analysis 3--Prototype Analysis <br>Reading Quiz 8

Week 9 March 4
Topic: <br>Analyzing Digital Rhetoric (At Home)<br><br>Readings: <br>None<br><br>Assignments: <br>Post Rough Draft of Final Project <br>Feedback Report

Week 10 March 118 
Topic: <br>Creating/Celebrating Digital Rhetoric/Reflection (F2F)<br><br>Readings: None<br><br>Assignments: <br>Final Project <br>Reflection

Tell me a joke
I don’t do that

I like rhetoric
I am so glad to hear that <img src=“/static/hooray.gif”></img>
```

## License
This source is free to use, but ChatterBot does have a license which still applies and can be found on the [LICENSE](https://github.com/gunthercox/ChatterBot/blob/master/LICENSE) page.


