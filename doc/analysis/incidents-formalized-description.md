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
## 22
```
class Shared disk group connection extends Direct instruction{
  group{
    context = AD-GROUPS,
    name =   9413-SHR-xxxxx
  }
  class disk{
    context = RSharedDISK:,
    address = \\gbw9061104\proj\xxxxxx
  }
}
```
## 23
```
class  Install software {
    name=IE8
}
```

## 26
```
class Pending installation extends Reinstall software {
	applicationToInstall = {
		name = Excel
	}
	Message about pending installation=  "windows installer preparing to install"
}
```
## 122
```
class  Install software {
    name = VPNClient
    class ClientInfo extends Target {
	Name = xxxx
	Location = xxxx
    }
    Service Tag = Migrated to vccnet
}
```
## 123
class Compound Problem{
    class Install Software{
        name=proxy_script
    }
    class problem solving ???{

    }

}

## 126
```
class User cannot perfom action extends desired state {
	failed action = class action {
		print from KDP
	}
	possible solution = class Reinstall software{
			applicationToInstall = {
			name = Excel
		}
	}
}
```

## 222
```
class  Install software Issue extends Install{
    error = VFTGCalled user, no answer
    class ClientInfo extends Target {
	Name = xxxx
	Location = xxxx
    }
    Service Tag = Migrated to vccnet
}

```

## 223
```
class LotRecieverProblem{
    class LOT OrderReciever{
       class Install{
           name=Catia.C3png-P2 v5
       }
    }
}
```

## 226
```
class Install software {
	Software = {
		name = IP communicator
	}
}
```


## 322
```
class  Update software Issue extends Install{
    error = unable to use application
    application = c3png
    priority = high
    class ClientInfo extends Target {
	Name = xxxx
	Location = xxxx
	Domain = xxxx
    }
    Service Tag = 9xxxb4Jxx
}

```

## 323
```
class LotRecieverProblem{
    class LOT OrderReciever{
       class Install software{
            name=  Adobe Acrobat Professional 7.0
            LOBAID=4440
       }
    }
}
```

## 326
```
class Reinstall software {
	Software = {
		name = IE8
	}
}
```

## 422
```
class LOTFailed  {
    Software =  Canalyzer(7.2 SP3)
    class ClientInfo extends Target{
	Receiver = xxxxx
    }
}
```

## 423
```
class LotRecieverProblem{
    class LOT OrderReciever{
       class Install software{
            name=  WinDVD(4.0)
       }
    }
}
```

## 426
```
class LotRecieverProblem{
    class LOT OrderReciever{
       class Install software{
            name = PAINTSHOPPRO(9.0)
       }
    }
}
```

## 522
```
class Install {
    application = IE
    version = 8
    class ClientInfo extends Target {
	Name = xxxx
	Location = xxxx
    }
}
```

## 523
```
class Install software {
    name=IE8
}
```

## 526
```
class LotRecieverProblem{
    class LOT OrderReciever{
       class Install software{
            name = Software Metering Report Tool(1.0)
       }
    }
}
```

## 622
```
class can not log {
    Software =  CATIA
    class errorInfo{
      type = missing file
      filename = xxxx
    }
    class ClientInfo extends Target{
	Name = xxxx
	Location = xxxx
        File location = xxx
    }
}
```

## 623
```
class Install software {
    name=Adobe Reader
}
```

## 626
```
class LotRecieverProblem{
    class LOT OrderReciever{
       class Install software{
            name = Hummingbird Host Explorer(11.0)
       }
    }
}
```

## 722
```
class No access {
    resource = home hard drive
    problem = not shared
    class ClientInfo extends Target{
	Name = xxxx
	Location = xxxx
        File location = xxx
    }
}
```

## 723
```
class  Reinstall software extends Problem description without desired state {
  application = VIDA All-in-one(2010 C Edition (SE))
}
```

## 726
```
class Install software {
    name=VIDA All-in-one 2010 C Edition (SE) (LOBAID: 5454)
}
```

## 822
```
class = Update software extends Direct instruction{
  class = Software{
    name =  eMS
  }
}
```

## 823
```
class LotRecieverProblem {
    class RemoveSoftware {
      application = Minitab version 15
    }
    class  Install software extends Problem {
      application = Minitab version 16
    }

}
```

## 826
```
class Reinstall software {
   installedApplication = Software{
    name =    C3PNG
  }
  applicationToInstall = Software{
    name =  C3PNG,
    version = latest version
  }
}
```

## 922
```
class = install{
  error = insufficient rights
  class = Software{
    name =  McAfee
    context = updates
  }
}
```

## 923
```
class  Install software extends Problem {
      application = VIDA on Web(1.0)
    }

```

## 926
```
Can not process, message about pending installation but without mentioning software, need user contact
```

## 1022

```
class = cant login{
  class = Software{
    name =  Business Warehouse
  }
}
```

## 1023
```
Unable to clarify, need specialist contact

```

## 1026
```
class No access {
  context = Software {
	name = SMS/SCCM client
  }
  access level = possibility to install configuration package
}
```

## 1122
```
class = Shared disk group connection extends Direct instruction {
  group{
    name = xxxx
  }
  disk{
    context = Shared DISK:,
    address = \\gbw9061108\proj\xxxx
}
```

## 1123
```
class = Shared disk group connection extends Direct instruction {
  group{
    name = 9413-SHR-VCC34514-R9413-SHR-VCC34514-AR
  }
  disk{
    context = Shared DISK:,
    address = \\gbw9061108\proj\9413-shr-vcc34500\CWM3-VCC34514
  }
}
```

## 1126
```
class No access {
  context =  Software {
	name = Lotus Notes
  }
  access level = access to Databases
}
```

## 1222
```
Unable to clarify, need specialist contact

```

## 1223
```
class LotRecieverProblem {
    class Install {
      application = Camtasia Studio
      version= 5.0
    }

}
```

## 1226
```
class User cannot perfom action extends desired state {
	failed action = class action {
		view something related quicktime via pictureviewer
	}
	possible solution = class Reinstall software{
			applicationToInstall = {
			name = quicktime
		}
	}
}
```

## 1322
```
Unable to clarify, some kind of conversation
```

## 1323
```
class Install {
      application = Lotus Notes Client
      version= 6.5.5
}
```

## 1326
```
class LotOrderNotDeliver {
}
```

## 1422
```
class = profiles{
   class = Profile{
      action = clean
      name = xxx1
   }
   class = Profile{
      action = clean
      name = xxx2
   }
   Service Tag:Migrated to vccnet 
}
```

## 1423
```
Need user clarification
```

## 1426
```
class Reinstall software {
   installedApplication = Software{
    name = VPN client
	version = 4.0.4
  }
  applicationToInstall = Software{
    name =  VPN client 4.0.4,
    version = 4.0.4
  }
}
```


## 1522
```
class Reinstall software {
   installedApplication = Software{
    name = Lotus Notes   
  }
  applicationToInstall = Software{
    name = Lotus Notes
  }
}
```

## 1523
```
Need user contact, or reinstall software, need instructions
```

## 1526
```
Unable to clarify, need specialist contact
```

## 1622
```
class Install {
      application = c3png
}
```

## 1623
```
User clarification required
```

## 1626
```
class User cannot perfom action extends desired state {
	failed action = class action {
		open a PDF file
	}
}
```

## 1722
```
Unable to clarify, need specialist contact
```

## 1723
```
class Alias Add extends Problem{
    name=wantedalias.example.com
    ip=127.0.0.1
}
```

## 1726
```
User clarification required
```

## 1822
```
class LotRecieverProblem {
    class Software {
      application =  Teamcenter and TC-vis VCC XP
      version= V5
    }

}
```

## 1823
```
class LotRecieverProblem {
    class Install {
      application = MatLab
      version= R2010b
    }

}
```

## 1826
```
class No access {
  context =  address {
	 Y/W/printers
  }
}
```