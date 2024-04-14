# Test task for Qorpo.world

## To run locally
1. `cd` into the root folder
2. Install the dependencies with `pip install -r requirements.txt`
3. edit `.env` file supplying the credentials to your local Postgres DB and app host and port if needed.
4. Run `alembic upgrade head` to add the necessary table to the DB.
5. Run `python -m src`

## To run via Docker
1. `cd` into the root folder
2. Run `docker compose up -d --build`


All the project settings can be edited in the `.env` file. The one included here is merely for your benefit, so you can launch the project with one (or two) command from the terminal. Normally I don't commit env-files :)
