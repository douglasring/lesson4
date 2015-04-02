c1 = ['Computer','- universal machine']

c2 = ['Program','''
	- tells computer exactly what to do
	- precise sequence of steps
	- useful, put them together to do what we want
	- precise sequence of steps
	- code, web browser, interpreter = all programs
	''']

c3=['Computation','''
	- very fast, billions of instructions 
	- light can travel ~30 cm in a nanosecond
	- light can travel less than a dollarbill length with a single fast CPU cycle
	''']

c4=['High-level language','''
	- python
	- requires an interpreter vs a compiler
	''']

c5=['Input','''
	- the grammar sent to the compiler or interperter''']

c6=['Compiler','''
		- generates a program that produces other programs
		- compile, then run program
		''']

c7=['Interpreter','''
	- compile run at same time
	-The programs will input to another program which is a Python interpreter that follows the instructions in your code and it does that by following the instruction in its code...
	''']

c8=['Grammar','''
	- unambigious, not verbose
	- the possible valid syntax and permutations available as input.  Terminal denotes end of tree permutation.
	- expression - legal use of the grammar 
		- print 1 + 1  is correct
		- print 1 + 1 + is not correct
		''']

c9=['Debugging','''
	- Python requires code be written with a very specific syntax. This means that small typos can lead to big problems!
	-The trick to dealing with programming mistakes (called "bugs") is not to avoid making them entirely. That's impossible. The trick is to develop a system for finding and fixing them.
	''']

c10=['Variables','''
	- Assign a name followed by an equal followed by an expression
	- Name is normally lowerclass
	- Name = Expression
	- Make our program easier to understand
	- Allow for re use
	- can change a value and new value will be assigned and used in order of assignment
 	- = Means Assignment, not equal per se
 	- Must be assigned before used
 	- Evaluates Right side of Equal then assigned to variable on Left
 	''']

c11=['Strings','''
 	- Sequence of characters enclosed in Quotes
 	- start and end with same type of quote, "" or ''
 	- Assigned the same as numbers
 	- The plus operator means Concatenate
 	- Strings and Integers can't be natively concatenated by addition
 	- Weirdly, we can multiply them!!
 	- We can INDEX these using extraction [], id starts @ 0
 	- name=Dave, name[0] will print D if i use print ...
 	- print name[-2] gives us v
 	-- Sub Sequence
 		- string[x:y]   - so x start and include, y stop but not include.  x: x to the end. :x - begin up to.  or : gives us whole word... don't use it.
 	- intro to find
 		- string.find(string)    --- output is first position or -1 if not found
 		print pythagoras.find('string')   "string" is what we're looking for and is at space 40.
 		- Hmmm all strings begin with '', or empty string
 	- passing two paramaters to find 
 	- 0 would be the same as we have been using
 	- <string>.find(<string>, <num>)  number of the position, the first occurence at or after it.

 	- Sometimes we need to use an empty string. "This is called an edge case in programming. It's a situation that doesn't come up too often (you usually don't need to use an empty string), but it does happen sometime.  It's easy to forget about edge cases and doing so is a 	common cause of bugs."

	- I should start using single quotes vs double
	- TRIPLE quotes to create multi line string

	-Abstract thinking cares for the unknown, such as using negative indexs VS specifics.  Both may solve a specific problem - but the general solves 'any problem'
	''']


c12=['Define Functions or Procedures','''
	what a function is
	how to make a function
		"def function(inputs):
			return result"
	how to use a function
		"function(foo)"
	when you should write a function
		-When you have a task that can be generalized and needs to be run several times / help avoid re writing routines.
	why functions are so valuable.   
		-Mapping input to output.

	<procedure> (<input>,<input2>) - known as inputs or arguments

	Needs to Provide a Return Statement unless it's mutating a list that we're calling later!!!
	''']


c13=['Use Procedures','''

	- Here's defining it: def rest_of_string(s):
		versus code like this:

	- Here's invoking it - print rest_of_string("audacity")

	-Procedure Composition
		Procedure definitio syntax
		using ouput of previous procedure in existing procedure  sum(sum(3))  for example

	-Questions to consider:
		What is a function (Dave calls them "procedures")?
			- A user defined procedure - something you create as a 'task' that returns the result of itself
		What is the difference between making and using a function?
			- Making is defining what inputs will be accepted and what to do with them
			- Calling the function is how it's used
		How do functions help programmers avoid repetition?
			- They allow tasks to be reused with different inputs and outputs without re writing the procedure
		What happens if a function doesn't have a return statement?
			- The work is processed but values are not returned for use later in the program

		Example:
		def square(x): 
		answer = x * x 
		return answer

	Don't forget that you can use triple quotes to create multi-line strings in Python!

	Python Function to output HTML
	- Break up the text and set as variables
	- SUM them together and return them
	''']

c14=['Procedural Thinking - IF and WHILE','''
	-Boolean  yes / no  --- true false
	= vs ==
	- if:
	- else:

	- shortcut
		def is_friend(name):
			return name[0] == 'D'
	 - this feals unnatural but it works equally well 

	 - Boolean "or" operator introduced when testing
	 def is_friend(name):
	 	return name[0] == 'D' or name[0] == 'N'

	 OR - only evaluates what it needs to - stops

	 Good tip on using the function we created called bigger.
	 We can use it to find the value of 3 numbers vs just our two simply
	 by calling itself.  bigger(bigger(3,4),100)
	 ''']

c15=['While Loop','''
	- while <expression>:
		<block>
	The block executes -as long as- the expression is true

	- BREAK - inside the loop - stops executing while loop and executes the code after that.
	''']

c16=['Modulules - Modularity','''
	breaking a big task into smaller pieces
	using functions that you have already written
	writing new functions to solve pieces of the bigger problem
	putting the "pieces" together to solve the bigger problem
	This is exactly what systems thinking is and it's one of they ways you're learning to think like a programmer.
	- Understand the Problem
		- Systematically Break Down The Problem
			- What's our Input?
				- Title and Description (PLURAL)
			- What's our desired Output?
				- HTML
	- We Need a Function to Convert Input to Output
		- Not a good idea to have one huge function do it
		- Break it down a bit smaller than this
			- Instead of converting All at Once
				- Lets do 1 "Concept" at a time
				- Work backwards from what we know we can do
			- Start with Concept's Title and Description >> to hHTML
				- Title 1 and Description 1 as a Single Function
				- Get input for Title and Description by their ordered #'s
				- Generate Text Title and Desc
				- This makes 4 smaller functions

	- Small modules that can be re used are extremely useful.  The Python iteration
		drove this point home as we built on finding TITLE and DESCRIPTION, converted it to HTML by pieces, and then ran a loop to output all the HTML.
		All of this was stored in simple STRINGS though.

	Data Lists and For Loops
	['Python', 'Python is a Programming Language']
	- There are strings and there are lists
	- Structured DATA
	Lists can be numbers, lists, characters, strings, etc
	a string - s='yabba!'
		- s[0]
		- s[2:4] >> 'bb'
	a list - p=['y','a','b','b'...]
		- p[0] >> 'y'
		- p[2:4] >> ['b','b']
		- square bracket, a list, seperated by commas
	accessing the list contents
	list.name[index][index][index]
	List Mutation - change the value of the list after its created
		- list[index]='new.value'    < < Pushes new value into index
		- a concern is other variables may refer to this same object
	List Aliasing
		- two different ways to refer to the same object

	List Appending
		-<list>.append(<element>)
	List Adding
		- list + list = list that appears with all added together via concat
		- the list wasn't changed - it just appears to be.
	List Len
		- len(<list>)

	For Loop 
		- For <name> in <list>:
			<block>
		- def blah(p):
			for e in p:
				print e

	Indexing
		- <list>.index(<value>)   <<< It returns the first occurance
		- but if it is not found, does not reutrn -1, but message stating <value> is not in list.
		- <value> in <list>  <<< Boolean True or False response
		- <value> not in <list>
		''']

c17=['Practice Part I','''
	Exploring List Properties: You'll explore the difference between concatenating two lists with the + operator and appending with .append(). You'll also be introduced to a new operator +=.

	- Good lesson on adding vs appending:
		def list_test(l1,l2,l3):
		    l1.append('a')
		    l2.append('a')
		    l2.append('b')
		    l2.append('c')
		    l3 = l3 + ['w']   < this one got me because I'm used to not using these brackets.  It also didn't mutate the l3.
		    return l3

	- lists -
	first_input = [1,2,3]
	second_input = [4,5,6]
	third_input = [7,8,9]
	''']

all_vars = vars()  # Make key/value to build one list below
all_concepts = [] # this will be my mutated list containing all 17 lists

'''
#def get_title(concept):   # Not required - here for sanity checks
#    title=concept[0]
#    return title
#    
#def get_description(concept):
#    description=concept[1]
#    return description
'''    

def make_one_list(size):  # I have 17 lists so this will be 17.  Called later by make all.
    i = 0
    while i < size:
        i += 1
        my_list_name = 'c' + str(i)
        all_concepts.append(all_vars[my_list_name])

def generate_concept_HTML(concept_title, concept_description):  # Modeled directly after example in class. Builds Divs.
    concept_html_open = '''
<div class="concept">
    <div class="section-title">
        ''' + concept_title
    description_html_open = '''
    </div>
    <div class="concept-content">
        ''' + concept_description
    concept_description_html_close = '''
    </div>
</div>'''
    
    htmlize = concept_html_open + description_html_open + concept_description_html_close
    return htmlize
    
def make_a_concept_to_HTML(concept):  # Input a concept at a time and output HTML for it
    rawtitle=concept[0]
    rawdescription=concept[1]
    return generate_concept_HTML(rawtitle,rawdescription)  # This is a powerful use of Return!!
    
def make_all_HTML(list_of_concepts): # Input all 17 full concepts as A list and spit out HTML
    html_ready = '' # I need to build up the HTML here and return ALL at the end
    for concept in list_of_concepts:
        html_ready = html_ready + make_a_concept_to_HTML(concept)
        #While htmlize builds up a concept at a time - i still need to build up all the html for all concepts and return them/it
    return html_ready   
    
def make_all(): # runs all functions needed for assignment
    make_one_list(17) # make all 17 into a single list here
    print make_all_HTML(all_concepts)
    return "Success!"

print make_all() # calls make_all to run program
