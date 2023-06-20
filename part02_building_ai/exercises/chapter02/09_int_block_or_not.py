#Let's suppose you have a social media account on Instagram, Twitter, or some other platform (just in case you don't, it doesn't matter. We'll fill you in with the relevant information). You check your account and notice that you have a new follower – this means that another user has decided to start following you to see things that you post. You don't recognize the person, and their username (or "handle" as it's called) is a little strange: John37330190. You don't want to have creepy bots following you, so you wonder whether to block them. To decide whether you should block the new follower, you decide to use the Bayes rule!

#Let's assume that 5% of your new followers are bots: this can be written as

#P(bot) = 0.05.

#Let's also assume that 80% of bot accounts have a username that includes an 8-digit number (like 37330190):

#P(8-digits | bot) = 0.8

#The last term that is required is the probability, P(8-digits), which is the probability that a new follower (either a bot or not) has an 8-digit number in their username. This probability would be quite hard to know or estimate directly. Instead, we may just know that real people who follow you usually don't have such a sequence in their username, so perhaps we have:

#P(8-digits | human) = 0.01.

#The nice thing is that we can now calculate P(8-digits) from the above information. The formula may look a little nasty at first sight, unless you're familiar with probability calculus, but it's quite friendly if you approach it with a smile:

#P(8-digits) = P(8-digits | bot) x P(bot) + P(8-digits | human) x P(human)

def p_human():
    p_bot = 0.05
    p_8digits_bot = 0.8
    p_8digits_human = 0.01
    value = (p_8digits_bot * p_bot + p_8digits_human * 0.95)
    return value

def p_bot_8digit():
    p_bot = 0.05
    p_8digits_bot = 0.8
    p_8digits_human = 0.01
    value = p_8digits_bot * p_bot / p_human()
    return value

print("P(human)", p_human(), "P(bot|8-digit)", p_bot_8digit())