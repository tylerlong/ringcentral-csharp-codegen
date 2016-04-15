# RingCentral C# Code Generator


## setup

Install pip: https://pip.pypa.io/en/stable/installing/

sudo pip install fabric


## commands

```
fab generate:<spec>,<language>
```

Examples:

```
fab generate # by default spec = advanced, language = csharp
fab generate:basic,javascript # generate javascript code for basic spec
fab generate:internal,java # generate java code for internal spec
```

The generated code is located in ./tmp directory.
