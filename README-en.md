# # spine-to-blender

![Anim](https://github.com/user-attachments/assets/756d70ff-3dc2-42c7-b20b-289163666614)

## README  

[中文](README.md) | [English (Using Translate)](README-en.md) 

## Install

(Recommended) Download the source code as a ZIP file directly | Select and download the file from Releases.

- Blender > Preferences > Add-ons > Install form disk > [spine-to-blender-main.zip]  

## Import

Blender Version: 5.0+ | Spine Version: 3.8 / 4.2  

1.Select the path to the [json / atlas / png] file exported by Spine

2.If you have multiple skins, you may need to manually enter the character name.

3.Set the name of the imported character.

4.Click [ Import Spine ]   

## Notice

This plugin can usually only handle relatively simple projects and only imports skeletons and meshes.

If all types are "region" (Skin attachments -> the mesh uses only 1 face/4 vertices)

Select the atlas folder and import using the <Re:Dive> type.

## Using Slots

1. The button to the left of "[Import Spine]" on the import interface can be used to import slot data.

2. The button to the right of "[Slot List]" on the slot interface can also open the hidden simplified import interface.

3. Select the target skeleton and enter the corresponding character name to obtain the bones/meshes from the slot data.

4. You can click the cursor to the left of the name to select the bone/mesh.

5. (You can quickly find relevant content using the mesh name: "Character Name - Slot - Attachment")

## Importing Animations (Only supported in Blender versions 4.4 and later)

Only keyframes for position / scale / rotation are supported.

Import as action data, non-linear animation can be used, and you can select the action and slot.

Information about the animation system in Blender version 4.4

https://docs.blender.org/manual/en/4.4/animation/actions.html

## About: spine-json-format

http://esotericsoftware.com/spine-json-format

## Known Issues

Skeletons using path constraints cannot be imported correctly.

When installing other versions, Blender needs to be restarted after uninstalling the plugin 

(restarting is not necessary when simply enabling or disabling the plugin).

When switching Blender's language, the plugin needs to be restarted for some UI translations to update correctly.

## Interface Preview

<img width="1601" height="1256" alt="info_en_us" src="https://github.com/user-attachments/assets/8acd58e7-bc0e-426d-816c-c10b9721dad0" />


