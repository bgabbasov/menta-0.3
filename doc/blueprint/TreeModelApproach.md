# Three models approach

## Problem
Currently it is recommended to use domain model design pattern and seems that it is quite reasonable to use one model through
whole application. This way application receives model objects via web-services interface, operates with received data than
stores it in DB(storage). All the same objects.

Web-services uses serialisation to transfer objects, this way seems reasonable to transfer other objects URI, rather then
transfer serialized referenced objects.

This is really not good idea to reference objects via URI, this usually implies using search in DB.

Storage implies implementation of special interfaces.

## Solution
Use three models:

 *. Interface: simplified with URI to reference other object.
 *. Application: ordinary complex domain model.
 *. Storage: special model implementing Stored Atoms.