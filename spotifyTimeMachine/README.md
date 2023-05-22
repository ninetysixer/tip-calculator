**Spotify Application using Python to create a playlist from the date entered by the user**

![image](https://github.com/semihdursungul/python_source_codes/assets/114025283/e5ab6902-d86d-4ae6-b84b-132ffb417703)

------------------------------------------------------------

Spotify Authentication
1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: http://spotify.com/signup/
2. Once you've signed up/ signed in, go to the developer dashboard and create a new Spotify App: https://developer.spotify.com/dashboard/ (PS: Redirect URI should be http://example.com)
3. Once you've created a Spotify app, copy the Client ID and Client Secret into your Python project. ![image](https://github.com/semihdursungul/python_source_codes/assets/114025283/85adf6ca-d536-40c8-839a-0acb0e2497ac)
4. Use http://example.com as your Redirect URI. You're looking to get the currentuser id (your Spotify username). As per the documentation, make sure you set the redirect URI in the Spotify Dashboard as well. Then it will take you to the page below, example.com and you need to copy the entire URL in the address bar:![image](https://github.com/semihdursungul/python_source_codes/assets/114025283/4c2950c8-a2c6-434e-823c-006a7f0689bf)
5. Finally, you need to paste the URL into the prompt in PyCharm:![image](https://github.com/semihdursungul/python_source_codes/assets/114025283/e8e4f2b8-554a-4df0-baba-8aa04928f33b)
6. Now if you close PyCharm and restart, you should see a new file in this project called token.txt ![image](https://github.com/semihdursungul/python_source_codes/assets/114025283/eece6539-06e9-4b4c-9669-3466bcb2cfdb)

