#########1111111111111

redirect V render


Both are totally different where the redirect gives the HttpResponseRedirect for the argument you have passed.

example

return redirect('https://example.com/')   in this we cant send context just will forward url to template or
outside websites i..e httpresponse

takes you to the https://example.com/ page
 where as render will take you to template 

 
 #3333
 
 media_root v media_url:
  
  media_root : is it specify the path where we are going to store uploaded file s form user 
   
   #genarally we are going to store mediafolder in projectfloder(projectfolder(parent)/mediafolder/(any child folder in it))
    
media_rul: this is used to access our file throught web browsers(to access files from webbrowsers)
    
    
    
    
