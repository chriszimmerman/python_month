#A Month With Python

Recently, I attended a philly.rb meetup where two talks were presented. One was on [civic hacking](http://www.slideshare.net/WilliamJeffries1/civic-hacking-on-rails) and one was on [language exploration](http://lanyrd.com/2015/mwrc/sdkmkc/#link-cbfhz). The talk on language exploration, titled "Make up your own 'Hello, world!'", inspired me to take a short-to-medium-term look into a new language.

In Justin Campbell's talk, he discusses the importance of learning new languages and how to go about it. Here's the gist: take up a new language and implement a nontrivial-yet-not-crazily-complex project. Try to embrace the idioms of the language while implementing your project so that you expand your mind, gain new perspective, and bring what you've learned back into the languages you currently work in. Justin's 'Hello world' of choice is a URL shortener. It's a nontrivial project and ensures that you'll be using a not insignificant portion of the language's features in order to implement it.

I decided to try this idea and timebox learning a new language to a month. The language I chose: Python. My version of 'Hello, world!': a [sudoku](http://en.wikipedia.org/wiki/Sudoku) solver. With a sudoku solver, you can learn how to get user input in several ways: from a file, from them typing it in by hand, from a web form. Once you get the input, you need to parse and validate the puzzle to see if it's already invalid. If not, you can attempt to solve it. As far as solving goes, I kept my solver simple and used a brute force algorithm to solve the puzzle. 

#Motivation

I regard Python and Ruby as the Pepsi and Coke of dynamically typed languages. They're pretty similar, or so I've heard. Before taking this journey, I only knew Ruby. I have used Ruby mostly as a scripting language to help automate tasks at my previous job. Other than that, I like to work on small side projects in Ruby. I find Ruby very enjoyable to work in. 

However, I wanted to make sure I wasn't missing out on anything. I heard that Python had fantastic libraries like SciPy and NumPy for support in science and math-related tasks. After attending this talk, I saw this as a great opportunity to get a taste for a language without heavily investing in it.


#Projects

For my first week or so with Python, I went through a good deal of [Automating the Boring Stuff With Python](https://automatetheboringstuff.com/) by Al Sweigart. Because of my Ruby background, I didn't find much in Python too unfamiliar. Going through this book got my head around fundamentals of Python like how to name variables/classes/methods and basic syntax. 

In my month with Python, I wrote a sudoku solver that is (mostly) unit tested and is capable of solving 9 by 9 sudoku puzzles. In doing this, I gained some experience with using Python's unittest library. Here is an example of a unit test written in Python:

	class SudokuPuzzleSolverTest(unittest.TestCase):

		def test_is_valid(self):
			puzzle = [
						[
							Square(1,1,1,1),
							Square(4,1,2,1),
							Square(3,1,3,2),
							Square(2,1,4,2)
						],
						[
							Square(3,2,1,1),
							Square(2,2,2,1),
							Square(4,2,3,2),
							Square(1,2,4,2)
						],
						[
							Square(4,3,1,3),
							Square(1,3,2,3),
							Square(2,3,3,4),
							Square(3,3,4,4)
						],
						[
							Square(2,4,1,3),
							Square(3,4,2,3),
							Square(1,4,3,4),
							Square(4,4,4,4)
						]
					]
			solver = Solver()
			self.assertTrue(solver.is_valid(puzzle))

#Impressions of Python

#Conclusion

#References
