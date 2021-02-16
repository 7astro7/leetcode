
# recall Maven image page says there are caveats (user creation and others)

FROM maven:latest

WORKDIR /preorder

COPY pom.xml pom.xml

COPY src src

#RUN mvn install

RUN mvn package

