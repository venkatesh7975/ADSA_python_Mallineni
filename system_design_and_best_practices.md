# System Design and Python Ecosystem - Interview Questions

This document covers System Design concepts, Software Architecture, REST APIs, Design Patterns, and common Python ecosystem tools.

## 1. Design Patterns in Python

**Q1. What is the Singleton Pattern? How would you implement it in Python?**
**A:** The Singleton pattern ensures that a class has only one instance and provides a global point of access to it. It is often used for configuration managers or database connections.
In Python, it can be implemented by overriding the `__new__` method or using a metaclass or a decorator.
```python
class Singleton:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance
```

**Q2. What is the Factory Pattern?**
**A:** A creational design pattern that provides an interface for creating objects in a superclass, but allows subclasses to alter the type of objects that will be created. It abstracts the instantiation process.
Instead of calling `Dog()`, you call `AnimalFactory.create_animal("dog")`.

**Q3. Explain the Observer Pattern.**
**A:** A behavioral design pattern where an object (the subject) maintains a list of its dependents (observers) and notifies them automatically of any state changes, usually by calling one of their methods. This is heavily used in event-driven systems (like GUI frameworks or Pub/Sub models).

## 2. REST APIs and Web Concepts

**Q4. What is a REST API?**
**A:** REST (Representational State Transfer) is an architectural style for designing networked applications. It relies on a stateless, client-server, cacheable communications protocol (almost always HTTP). REST APIs map CRUD (Create, Read, Update, Delete) operations to HTTP verbs:
- **GET:** Retrieve a resource
- **POST:** Create a new resource
- **PUT/PATCH:** Update a resource
- **DELETE:** Delete a resource

**Q5. What is the difference between PUT and PATCH?**
**A:** 
- **PUT:** Completely replaces an existing resource. If you send a PUT request without all the fields, the missing fields should be set to null/empty by the server.
- **PATCH:** Applies partial modifications to a resource. You only send the fields you want to update.

**Q6. What does it mean for an API to be "stateless"?**
**A:** It means the server does not store any state about the client session on the server-side. Each request from the client to the server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Authentication tokens (like JWT) are sent with every request for this reason.

## 3. System Design Basics

**Q7. Explain the difference between Horizontal and Vertical Scaling.**
**A:** 
- **Vertical Scaling (Scaling Up):** Adding more power (CPU, RAM, Storage) to an existing machine. It is simple but has a hard physical limit and can cause downtime during the upgrade.
- **Horizontal Scaling (Scaling Out):** Adding more machines (nodes) into your pool of resources. It provides near-infinite scaling and high availability, but significantly increases architectural complexity (requires Load Balancers, distributed databases, etc.).

**Q8. What is a Load Balancer?**
**A:** A Load Balancer acts as the "traffic cop" sitting in front of your servers and routing client requests across all servers capable of fulfilling those requests in a manner that maximizes speed and capacity utilization and ensures that no one server is overworked (which could degrade performance). Examples include NGINX, HAProxy, or AWS ELB.

**Q9. What is Caching? Where can it be applied?**
**A:** Caching is the process of storing copies of files or data in a temporary storage location (cache) for fast access. It reduces latency and database load.
- **Client/Browser Cache:** Storing static assets locally.
- **CDN (Content Delivery Network):** Caching static files geographically closer to users.
- **Application/In-Memory Cache:** Using Redis or Memcached to store frequent DB query results or session data.
- **Database Cache:** DB engines' internal caching.

**Q10. What is the CAP Theorem?**
**A:** The CAP theorem states that a distributed data store can only simultaneously provide two of the following three guarantees:
- **Consistency:** Every read receives the most recent write or an error.
- **Availability:** Every request receives a (non-error) response, without the guarantee that it contains the most recent write.
- **Partition tolerance:** The system continues to operate despite an arbitrary number of messages being dropped or delayed by the network between nodes.
Since network partitions are inevitable, architects must usually choose between Consistency and Availability (CP vs AP).

## 4. Python Ecosystem & Best Practices

**Q11. Explain virtual environments in Python (e.g., `venv`).**
**A:** A virtual environment is an isolated Python environment that allows you to install packages and dependencies for a specific project without affecting the global Python installation or other projects. This solves the "dependency hell" problem where different projects require conflicting versions of the same library.

**Q12. What is `pytest`? How is it different from `unittest`?**
**A:** `pytest` is a mature, full-featured Python testing tool.
- `unittest` is built into the standard library but requires a lot of boilerplate code (requires creating classes and using specific assertion methods like `self.assertEqual()`).
- `pytest` allows writing tests as simple functions, uses plain `assert` statements (with detailed introspection on failure), supports powerful fixtures, and has a rich ecosystem of plugins.

**Q13. How would you profile a Python application to find performance bottlenecks?**
**A:**
- **cProfile:** The built-in profiler that provides statistics on how often and for how long various parts of the program executed.
- **line_profiler:** A third-party tool that gives line-by-line timing.
- **memory_profiler:** A tool to monitor memory usage of a Python program line-by-line.

**Q14. What are the key differences between Django and Flask?**
**A:**
- **Django:** A "batteries-included" full-stack web framework. It comes with a built-in ORM, admin panel, authentication system, and enforcing a specific project structure. Great for large, monolithic applications built quickly.
- **Flask:** A "microframework". It provides only the essentials (routing, request handling) and leaves the choice of database (SQLAlchemy), authentication, and project structure up to the developer. Great for small applications, microservices, or APIs.
