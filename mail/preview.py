'''
MUA(mail user agent).
MTA(mail transfer agent): email server provider(如网易，腾讯等)。
MDA(mail deliver agent): email到达MDA后，要收取邮件，必须通过MUA从MDA上将邮件取到自己的电脑上。
An Email trip is:
     sender --> MUA --> MTA --> MTA... --> MDA <-- MUA <-- receiver


编写程序发送或者接受邮件：
    1、编写MUA将邮件发送到MTA.
    2、编写MUA从MDA上收取邮件.
    
    发邮件时，MUA和MTA使用的协议是SMTP(Simple Mail Transfer Protocol), MTA-->MTA也是SMTP协议。
    收邮件时，MUA和MDA使用的协议有两种：
        1、POP(Post Office Protocol):目前版本3，俗称POP3.
        2、IMAP(Internet Message Access Protocol): 优点是不但能够取邮件，还能直接操作MDA上存储的邮件。
        
    发送邮件：
        邮件客户端在发送邮件时，需要配置SMTP服务器，也就是要发送到哪个MTA上。
        假设你正在使用163的邮箱，你就不能直接发到新浪的MTA上，所以，你得填163提供的SMTP服务器地址：smtp.163.com，
        为了证明你是163的用户，SMTP服务器还要求你填写邮箱地址和邮箱口令，
        这样，MUA才能正常地把Email通过SMTP协议发送到MTA。
    
    接收邮件：
        从MDA收邮件时，MDA服务器也要求验证你的邮箱口令，确保不会有人冒充你收取你的邮件，
        所以，Outlook之类的邮件客户端会要求你填写POP3或IMAP服务器地址、邮箱地址和口令，
        这样，MUA才能顺利地通过POP或IMAP协议从MDA取到邮件。
        
        

    
'''