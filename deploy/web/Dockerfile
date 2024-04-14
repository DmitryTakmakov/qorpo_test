FROM python:3.11 as requirements_extractor

RUN pip install pdm
COPY pdm.lock pyproject.toml /
RUN pdm export --without-hashes -f requirements -o /requirements.txt

FROM python:3.11

ENV PYTHONUNBUFFERED=1
COPY --from=requirements_extractor /requirements.txt /
RUN pip install -r requirements.txt
RUN mkdir /src/
ADD src /src/
COPY /deploy/web/entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
