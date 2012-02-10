# Goal
Class Goal is a SemanticNode that represent goal of the request. 

```
class = Insufficient disk space extends Problem description without desired state {
  driveName = c,
  networkAddress = {
    context = driveName,
    address = MEL123
  }
}
```

Here we have a goal 'Insufficient disk'. It will be connected to set of critics what will be automatically activated

```
class = Reinstall software extends Direct instruction AND Problem description without desired state {
  Software {
    name = Produkt Manageron
  }
}
```

Goal is a 'Reinstall software'

```
class = Shared disk group connection extends Direct instruction {
  group{
    context = AD-GROUPS,
    name =  9413-SHR-null55100-AR9413-SHR-null55100-R
  }
  disk{
    context = Shared DISK:,
    address = \\gbw9061117\proj\9413-shr-null55100
  }
}
```

Goal is Shared disk group connection

# Class description

![Goal structure](https://github.com/menta/menta-0.3/raw/master/doc/informal/uml/images/GoalTraining.png)

1.  Resources - is a KLine that contains suitable Critics to be activated
