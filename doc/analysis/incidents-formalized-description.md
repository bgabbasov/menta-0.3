# Incident analysis result

## 2
```
class = Invalid Login extends Problem description without desired state{
  login = snill9,
  application = T-centre
}
```

## 3

```
class = Connectivity problem extends Problem description without desired state{
  device = 3G modem,
  precondition = after migration
}
```

## 4

```
class = Can not find extends Problem description without desired state{ // this class seems to be obscure
  object = "Outlook pst file backup",
  objectType = icon
}
```

## 5

```
class = Reinstall software extends Direct instruction{
  class = Software{
    context = application,// this could be redundant
    name = Adobe Photoshop
    version = CS3
  }
}
```

## 6

```
Can not process need attachment message.
```

## 7

```
class = Wrong application has been installed extends Reinstall software with desired state {
  installedApplication = Software{
    context = ordered instead,
    name =   Wordfinder,
    version = Business Economical
  }
  applicationToInstall = Software{
    context = received,
    name = Wordfinder,
    version = Tehcnical
  }
}

```

## 8

```
class = Insufficient disk space extends Problem description without desired state {
  driveName = c,
  networkAddress = {
    context = driveName,
    address = MEL123
  }
}
```

## 9
```
class = Reinstall software extends Direct instruction AND Problem description without desired state {
  Software {
    name = Produkt Manageron
  }
}
```

## 10

```
class Reinstall software extends Problem description with desired state {
  application = PDF
}
```

## 11

```
Can not process, need the instruction what to do with software mentioned.
```

## 12

```
class = Shared disk group connection extends Direct instruction {
  group{
    name = 9413-SHR-R9413-SHR-VCC55101-AR
  }
  disk{
    context = Shared DISK:,
    address = \\eee9061117\proj\9413-shr-vcc55100\88625_Fire_Protection-VCC55101
  }
}
```

## 13
```
class = Reinstall software extends Problem description without desired state {
  application = Adobe Reader
}
```

## 14

```
class = Invalid time extends Problem without desired state{
  Software = {
    name = Outlook
  }
}
```

## 15

```
Can not process: No incident description available.
```

## 16

```
class = Shared disk group connection extends Direct instruction {
  group{
    context = AD-GROUPS:,
    name =  9413-SHR-S19413-SHR-VCC46701-AR9413-SHR-46701-R
  }
  disk{
    context = Shared DISK:,
    address = \\eee9061110\proj\9413-shr-null46700\Managment_Team-null46701
  }
}
```

## 17

```
class = Setup Wi-Fi extends Request for assistance{
 machine = {
   address = GOBLIN
 },
 machine = {
   name = PET
 }
}
```

## 18
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

## 19
```
class = Can not find extends Problem description without desired state{
  software {
    name = null
  }
}
Can not process the request, need an application name.
```

## 20
```
class Shared disk group connection extends Direct instruction{
  group{
    context = AD-GROUPS,
    name =   9413-SHR-null40600-AR9413-SHR-null40600-R
  }
  class disk{
    context = Shared DISK:,
    address = \\gbw9061104\proj\9413-shr-null40600
  }
}
```
