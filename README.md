if-else-tennis
==============

This is a project using git commit histories to demonstrate how a contrived
piece of code can change over time as requirements for the code also change.

The code is a function that returns the name of Grand Slam men's singles
champions in the ten years spanning from 2004 to 2013.

After the code settles into an up-to-date state (as of the end of 2013), it's
refactored to adjust the semantic meaning of the code with post prior knowledge
of how the tournament histories progressed. While logically the output of the
function should not be altered (given the same input space), the refactoring is
aimed to require fewer changes for future results -- at least in the next few
years.

Ultimately, this may be interpreted as a programmatic to answering the question
"Is Roger Federer the Greatest Tennis Player of All Time?"
