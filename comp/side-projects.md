# Side Projects Todo

Whatever is finished should not be here. Whatever hasn't started should not be here.

## [Game Comment](https://games.tasuki.org/)

- Comment editing
- Show game tree

## [ContinuGo](https://continugo.tasuki.org/)

- Sitting pretty at ~2k loc. Perhaps could be considered finished. But...
- Wouldn't it be cool if there was a way to play online without passing the urls around? What'd it take?
	1. A (simple) backend 🙈
	2. Frontend accommodations: a way to create a game.
	3. Frontend accommodations: a mode to allow exploring ahead without submitting the move. An idea: just draw circles. But then, how does one submit a move?
	4. Real time updates. Server-Sent Events?
	5. Absolutely no chat, but if anyone uses this they'll want chat 🙈
- If we had a backend, it should be easy to create a tournament. Why even have a backend if not for a tournament? But...
	1. A tournament would definitely require user accounts.
	2. And (server-side) time management.
	3. And server-side move validation and final scoring to determine the game result.
	4. Probably would have to finally implement the ko (ok, easy).

## Iso-Maze

- Try rewriting the visuals into shadertoy-style everything-in-the-fragment-shader.
- Create a campaign. At least 10 levels.
- Create a mobile app perhaps?
