# Stackelberg (Leader–Follower) Games

## Idea

In a Stackelberg game one player (the **Leader**) moves first and commits to a strategy. The other players (**Followers**) observe the Leader’s choice and then best-respond.

The Leader anticipates the Followers’ reaction and chooses the action that maximizes its own payoff given that reaction.

## Energy example used here

- **Leader** = aggregator or utility that sets a price signal.
- **Followers** = prosumers that decide how much to consume (or discharge) given that price.

The Leader solves:

```
max_price  revenue(price, demand(price)) − cost(price)
```

where `demand(price)` is the sum of the Followers’ best responses.

This is a classic hierarchical optimization problem that appears in demand-response programs and in some retail pricing schemes.
