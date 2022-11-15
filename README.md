# Intro
New Dex was planned to be a debugging suite. Only the Explorer part is completed, probably nothing else will be.

It was discontinued more than a year ago, might as well just release.
	
This is the final version of this script.
You are encouraged to edit, fork, do whatever with this. I pretty much won't be updating it anymore. Pull requests probably won't be accepted.
Though I would highly appreciate it if you kept the credits in the script. I put a lot of hours into this during the time I worked on it.

I have converted this from ModuleScript format (I used to develop this in studio) to a file format, to make it easier for whoever wants to continue or edit this. Build instructions are below.
If you feel too lazy to build, I have provided the built version in the releases.

## Notes
- There is no cloneref protection, add it if you want
- It may be detected by more stuff; I don't know what these detections are nor am I interested in fixing it
- Some stuff can be optimized further (ex: explorer node add/remove), it's up to you if you want to do it
- Some stuff may break when roblox releases deferred events. Ex: Selecting a duplicated instance

## To Build
1. Ensure you have Python 3 (I use 3.9.0)
2. Run build.py
3. The executable script will be created as out.lua

## High Level Roadmap
List of stuff that I planned do before I realized that I shouldn't be working on this anymore. If you are really interested in continuing this, you could add this stuff and make New Dex the ultimate utility that I wanted it to be. I might be forgetting stuff since I haven't worked on it for so long.
- Terminal
	* basically command interface with useful commands (non troll or gross) to get around
	* each command has all its funcs, state contained in a table
- Debugging interface
	* more than just a remotespy
	* you can choose to hook any metamethod, instance func/prop/event/callback, or any func
	* logging args/returns of those funcs (like a remotespy)
	* realtime editing of your hooks (allowing easy debugging: arg apoofing, return spoofing, unhook) using script editor
	* scripted filters
	* save/load these configs
	* default template would be set up to function like a remotespy
- Explorer
	* smart autofill for search
	* more filters for search
	* bookmarking / starring insts
	* a lot of the things in right click that i planned but didn't finish
- Properties
	* Copy value on clipboard (what is displayed in the box, or formatted to be pasted into lua)
	* Select object properties in explorer
	* Tag Editor (I saw the new one on devforum recently, would be better as its own window)
- Data viewing & finding
	* the const, upval, etc searching
	* list references of userdata, table, function (i wanted to make it so you can easily explore the references, opens new tab for each individual object)
	* detailed view of selected function (env, consts, upvals, decompiled src, script path, references)
	* easily create constant signatures
	* thread exploring
- Script viewer/editor
	* some decent autofill
	* info bar at bottom (line of error, line count, col count, etc)
- Reference
	* interactive api docs for instance props, funcs, etc
	* docs for some other stuff such as 'Dex' global, plugin api, executor api, etc
	* some tutorials with text, pics, and video (not doing video until roblox removes limit of 3 playing videos)
- Plugins
	* Easy way to add some stuff such as right click options, search filters, commands, etc
	* Access to dex's api for windows, modules, etc

## Missing stuff from old Dex
Features that existed in old Dex that I didn't get to make. These should be the first things you add if you plan to continue / edit this.
- Click to select
- Saving (instance specific in right click menu, and a menu for whole map saving)
- Settings menu
- Tabs in script viewer

## Server
If you would like to find more information (such as outdated docs), or talk to others interested in this script, you may join the server:<br>https://discord.io/zinnia<br>
Note that very limited to no support will be provided.
