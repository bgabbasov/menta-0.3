# 1
User gets Invalid Login when trying to logon to Exampleproject. He has got a new password and changed it on the new ID page but it still does not work.
## Metafor
ok.  i created a new agent called User.  i added the ability for User to get.  
the User can get using Invalid Login.  
ok.  i created a new agent called Invalid Login.  i added the ability for Invalid Login to when try.  ok.  i added the ability for Invalid Login to get.  the Invalid Login can get using new password.  ok.  i added the ability for Invalid Login to change.  the Invalid Login can change using new password and on new ID page.  ok.  i created a new agent called new ID page.  i added the ability for new ID page to not work.
* Partly correct:* 
Incorrect parts: 
     class Invalid_Login:
          def when_try():
               pass
               
          def get(new_password):
               pass
               
          def change(new_password, new_CDSID_page):
               pass
Those methods should be in class User. 
Teamcenter was not mentioned.

## Montylingua
(NX User/NNP NX) (VX gets/VBZ VX) (NX Invalid/NNP Login/NNP NX) (VX when/WRB trying/VBG VX) to/TO logon/RB to/TO (NX Exampleproject/NNP NX) ./.
(NX He/PRP NX) (VX has/VBZ got/VBN VX) (NX a/DT new/JJ password/NN NX) and/CC (VX changed/VBN VX) (NX it/PRP NX) on/IN (NX the/DT new/JJ ID/JJ page/NN NX) but/CC (NX it/PRP NX) (VX still/RB does/VBZ not/RB work/VB VX) ./.
*Correct*
 
# 2
Problem with 3G modems after migration. Mobile connection not possible. Ensure that no other programs are using your selected device, and try again in a short while. The user is a agent working at the UK helpdesk, please see the email attached to this ticket for more info.
## Metafor
ok.  i created a new agent called other program.  i added a field called select device to other program.  ok.  i added the ability for other program to try.  ok.  i created a new agent user that is a kind of agent agent.  ok.  i created a new agent called agent.  i added the ability for agent to work.  the agent can work using at UK helpdesk.  ok.  i added the ability for agent to please.  the agent can please using see and email.  ok.  i created a new agent called email.  i added the ability for email to attach.  the email can attach using to ticket and for more info.
*Partly correct*
Output not mentioned: Problem with 3G modems after migration. Mobile connection not possible.
## Montylingua
(NX Problem/NNP NX) with/IN (NX 3G/CD modems/NNS NX) after/IN (NX migration/NN NX) ./.
(NX Mobile/NNP connection/NN NX) (NX not/RB possible/JJ NX) ./.
(NX Ensure/NNP NX) that/IN (NX no/DT other/JJ programs/NNS NX) (VX are/VBP using/VBG VX) (NX your/PRP$ selected/VBN device/NN NX) ,/, and/CC (VX try/VB again/RB VX) in/IN a/DT (NX short/JJ NX) while/IN ./.
(NX The/DT user/NN NX) (VX is/VBZ VX) (NX a/DT agent/NN NX) (VX working/VBG VX) at/IN (NX the/DT UK/NNP helpdesk/NN NX) ,/, (VX please/VB VX) (NX see/NN NX) (NX the/DT email/NN NX) (VX attached/VBN VX) to/TO (NX this/DT ticket/NN NX) for/IN (NX more/JJR info/NN NX) ./.
*Correct*

# 3
User is missing "Outlook pst file backup" icon on her desktop.
## Metafor
i didn't understand that.
*Wrong*
Rephrase helps: User miss icon in her desktop.
## Montylingua
(NX User/NNP NX) (VX is/VBZ missing/VBG VX) (NX QUOTE_llVIMgeUay/NNP icon/NN NX) on/IN (NX her/PRP$ desktop/NN NX) ./.
*Correct*

# 4
User has been on a trip and is now back, please install the application now.
## Metafor
ok.  i created a new agent User that is a kind of on trip agent.  i didn't understand that.  ok.  i added the ability for User to install.  the User can install using application.
*Wrong*
User is not the trip agent, User should not install the application, system should to it.
## Montylingua
(NX User/NNP NX) (VX has/VBZ been/VBN VX) on/IN (NX a/DT trip/NN NX) and/CC (VX is/VBZ now/RB back/RB VX) ,/, (VX please/VB install/VB VX) (NX the/DT application/NN NX) now/RB ./.
*Correct*

# 5
See attachment for error message. LAB95 - Provning rekveo planering Please assist user, and investigate! 
## Metafor
i created a new agent called Metafor.  i added the ability for Metafor to See.  the Metafor can See using attachment and for error message.  ok.  i created a new agent called Provning rekveo planering.  i added the ability for Provning rekveo planering to Please.  the Provning rekveo planering can Please using assist user.  ok.  i added the ability for Provning rekveo planering to investigate.
*Partly correct*
Second part of the phrase is wrong, possibly because of syntax error. 
## Montylingua
(VX See/VB VX) (NX attachment/NN NX) for/IN (NX error/NN message/NN NX) ./.
(NX LAB95/CD NX) -/: (NX Provning/NNP rekveo/NN planering/NN NX) (VX Please/VB VX) (NX assist/NN user/NN NX) ,/, and/CC (VX investigate/VB VX) !/. ./.
*Wrong*

# 6
User had received wrong application. User has ordered Wordfinder Business Economical for her service tag 7Q4TC3J, there is completed order in LOT with number 18125. However she received wrong version, she received Wordfinder Tehcnical instead of Business Economical. Please assist.
## Metafor
ok.  i created a new agent called User.  i added the ability for User to receive.  the User can receive using wrong application.  ok.  i added the ability for User to order.  the User can order using Wordfinder Business and Economical and for service tag.  i didn't understand that.  ok.  i created a new agent called LOT.  i added the ability for LOT to receive.  the LOT can receive using wrong version.  ok.  the LOT can receive using Wordfinder Tehcnical.  ok.  i added the ability for LOT to Please.  the LOT can Please using assist.
*Partly correct*
Lot can not order and receive, but the user can, bug in DEICTIC STACK.
## Montylingua
(NX User/NNP NX) (VX had/VBD received/VBN VX) (NX wrong/JJ application/NN NX) ./.
(NX User/NNP NX) (VX has/VBZ ordered/VBN VX) (NX Wordfinder/NNP Business/NNP NX) (NX Economical/JJ NX) for/IN (NX her/PRP$ service/NN tag/NN NX) (NX 7Q4TC3J/JJ NX) ,/, (NX there/EX NX) (VX is/VBZ completed/VBN VX) (NX order/NN NX) in/IN (NX LOT/NNP NX) with/IN (NX number/NN 18125/CD NX) ./.
However/RB (NX she/PRP NX) (VX received/VBD VX) (NX wrong/JJ version/NN NX) ,/, (NX she/PRP NX) (VX received/VBD VX) (NX Wordfinder/NNP Tehcnical/NNP NX) instead/RB of/IN (NX Business/NNP NX) (NX Economical/JJ NX) ./.
(VX Please/VB VX) (NX assist/NN NX) ./.
*Correct*

# 7
Laptop - user has almost full C:\ but when he looks in the properties of the files and folders on C:\ they are only 40GB and he has a 55GB drive.
## Metafor
i didn't understand that.  ok.  i created a new agent called he.  i added the ability for he to look.  the he can look using in property and of file and folder and on C.  ok.  i created a new agent file and folders that is a kind of 40GB agent.  i didn't understand that.
*Partly correct*
System did not parse first sentence.
## Montylingua
(NX Laptop/NN NX) -/: (NX user/NN NX) (VX has/VBZ almost/RB VX) (NX full/JJ C/NN NX) :/: (NX \/NN NX) but/CC when/WRB (NX he/PRP NX) (VX looks/VBZ VX) in/IN (NX the/DT properties/NNS NX) of/IN (NX the/DT files/NNS and/CC folders/NNS NX) on/IN (NX C/NN NX) :/: (NX \/NN NX) (NX they/PRP NX) (VX are/VBP only/RB VX) (NX 40GB/CD NX) and/CC (NX he/PRP NX) (VX has/VBZ VX) (NX a/DT 55GB/NN drive/NN NX) ./.
*Correct*

# 8
User cannot find Produkt Manageron start menyplease reinstall. 
## Metafor
ok.  i created a new agent called User.  i added the ability for User to not find.  the User can not find using Produkt Manageron.  ok.  i created a new agent called Produkt Manageron.  i added the ability for Produkt Manageron to start.  the Produkt Manageron can start using menyplease.  ok.  i created a new agent called menyplease.  i added the ability for menyplease to reinstall.
*Partly correct*
Syntax error caused the system to fail parse menyplease reinstall: wrong class menyplease (syntax error), and it's methods reinstall.
## Montylingua
(NX User/NNP NX) (VX can/MD not/RB find/VB VX) (NX Produkt/NNP Manageron/NNP NX) (VX start/VB VX) (NX menyplease/NN NX) (VX reinstall/VB VX) ./.
*Correct*

# 9                                   
User needs to have pdf 995 re-installed please.
## Metafor
i didn't understand that.  ok.  i created a new agent called re-installed.  i added the ability for re-installed to please.
*Wrong*
System failed to process User needs to have phrase.
## Montylingua
(NX User/NNP NX) (VX needs/VBZ to/TO have/VB VX) (NX pdf/NN 995/CD NX) (NX re-installed/JJ NX) (VX please/VB VX) ./.
*Partly correct*
Please is not a verb.

# 10
Failed LOT. 
## Metafor
None
## Montylingua
(NX Failed/NNP LOT/NNP NX) ./.
*Correct*

           
