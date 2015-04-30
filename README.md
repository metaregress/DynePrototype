# DynePrototype

A digital prototype of a game I worked on in college with a friend. One of the problems we ran into was mechanics that were pretty dang complicated for a tabletop game, so I figured I'd have a go at porting it to a digital medium and seeing how it felt.

# Code Structure
Dyne.py is the main file. It usually contains an example scenario. For now it's just showing off functionality, until I can figure out how I want to handle input. It contains the game class, which is responsible for event management. Later on, it will deal with turns and win conditions.

DamageDealtEvent.py is the first event I've created. I'm still not sure what it is that all events have in common such that I can abstract to a single Event parent class.

Character.py describes a character. Until it gets a profession and some abilities, it's just a half-initialized ball of stats with a move and attack ability.

Profession.py is a container for profession information. The actual professions are detailed in the professions folder. Professions can be applied to Characters, conferring all their bonuses to the characters.

Items are similar to professions in their structure; Items.py shows how they are built, and then instances are created from the py/json files in the items folder. I'm thinking about moving this to a monolithic ItemLoader class that will just grab all the json and build a dict of items, but that can be addressed later.
