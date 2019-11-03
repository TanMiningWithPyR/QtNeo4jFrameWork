# QtNeo4jFrameWork

## PyQt5
Qt5 is set of cross-platform C++ libraries that implement high-level APIs for accessing many aspects of modern desktop and mobile systems. These include location and positioning services, multimedia, NFC and Bluetooth connectivity, a Chromium based web browser, as well as traditional UI development.
PyQt5 is a comprehensive set of Python bindings for Qt v5. It is implemented as more than 35 extension modules and enables Python to be used as an alternative application development language to C++ on all supported platforms including iOS and Android.

## Neo4j
Neo4j is one of the popular Graph Databases and Cypher Query Language (CQL). Neo4j is written in Java Language. In Neo4j, data is persisted as nodes and relationships.

## Object-oriented
As we know, contemporary mean for software design is object-oriented and python is an absolute object-oriented language. When designing an APP, an SQL database is considerd. But the data modelling of SQL database is not object-oriented. So usually we use ORM to map object into data table, such as SQLAlchemy. 

For my perspective, we can map Python's objects and Python's relationship between objects into Neo4j's nodes and relationships directly. Then we unify the methodology in one software designing no matter what on client, server or db. 


## Software Architetecture

### Configured Tables of Objects Registration

The core of software architetecture is the configured tables of objects registration (__CTOR__). The definitions of front end, back end and database are dependent to the CTOR.

The CTOR includes the following items:

#### Use Case Name
Definitions of use cases are the beginning of the Object-oriented analysis. In the framework, for the front end, the use case names should be reflected in the tree menu at the left of the whole window; for the back end, the use case names can be accord with the web service names consisted of URL routes. Therefore, the use cases are also regarded as the modules of the software system. They could be installed or discarded at no matter time or no matter where in the future.

In UML, there are four kinds of relationships among use cases: 

1. extends
2. include
3. realize
4. refine

They would become the reason why we should add sub items in the tree menu.

#### Class Name 

#### Class Structure

#### Class Relationship Name

#### Class Relationship Structure


