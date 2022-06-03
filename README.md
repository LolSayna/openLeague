# openLeague
Experimenting with different tools arround data analysis and league.

Runs of python, other tools:
- Github for version control
- Docker for deployment as a single containers

Data input:
- riot api WIP
- leaguepdia api WIP
- lolpros api WIP
- web scraping WIP

Data processing:
- sqlite database
- python+pandas+numpy ?WIP?

Data output:
- simple CLI
- Discord bot WIP
- web applicantion ?WIP?

Other TODO:
- how to handel api keys and credentials
- python packaging? with __init__.py and main functions, not sure yet how
- pytests & docs. How to do pytest with multi-stage or how

- Docker: healtcheck? together with other debuging

# Workflow
Github via UI
- stage
- commit + message
- push

Docker Testing:
- docker build -t open_league .
- docker run open_league
Debugging:
- docker run -it open_league /bin/bash