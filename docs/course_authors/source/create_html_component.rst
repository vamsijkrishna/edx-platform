.. _Working with HTML Components:


#############################
Working with HTML Components
#############################

*******************
Overview
*******************

You use HTML components to add and format text, links, images, and more in your course. By default, Studio has four HTML component templates. 

* :ref: `Text Template`: The most commonly used HTML component. COMPLETELY BLANK - NO PLACEHOLDER TEXT
* :ref: `Announcement Template`: A template that contains placeholder text and formatting that helps you create an announcement for your course.
* :ref: `Anonymous User ID Template`: 
* :ref: `Zooming Image Template`


**Can do the same things with all these templates because the component is just an HTML editor.**

See the following topics:

* :ref:`Create an HTML Component`
* :ref:`The User Interface`
* :ref:`Use the Announcement Template`
* :ref:`Use the Anonymous User ID Template`
* :ref:`Add a Link in an HTML Component`
* :ref:`Add an Image to an HTML Component`

.. note:: Ensure you understand the chapter :ref:`Organizing Your Course Content` before working with HTML components.

.. note:: Review :ref:`Best Practices for HTML Markup` before adding HTML components to your course.






.. _The User Interface:

*****************************************
The HTML Component User Interface
*****************************************

The HTML component editor has two views: **Visual view** and **HTML view.** By default, every HTML component opens in Visual view. To switch between Visual view and HTML view, click the  tab in the upper-right corner of the component editor.

.. image:: Images/HTMLEditorTabs.gif

==============
Visual View
==============

:ref: :ref: :ref: :ref: :ref:

START HERE

The Visual view provides a “what you see is what you get” (WYSIWYG) editor for
editing a pre-formatted version of the text. 

.. image:: Images/HTMLEditor_Visual.gif

Use the buttons at the top of the Visual editor to change the formatting as needed. 
For example, you can enclose the title in heading tags, create bulleted or numbered lists, 
or apply bold, italic, or underline formatting. 

==============
HTML view
==============
The HTML view allows you to edit HTML code directly.

.. image:: Images/HTMLEditor_HTML.gif

.. note:: Studio processes the HTML code entered when saving it and before rendering
  it. Make sure that the text you create looks the way you expect if
  you go back and forth between the Visual and HTML views.

.. _Create an HTML Component:

*****************************
Create an HTML Component
*****************************

To create a new HTML component in an existing unit, ensure the unit is private.  
For more information on public and private units, see :ref:`Public and Private Units`.

#. Under **Add New Component**, click the **html** icon.

  .. image:: Images/NewComponent_HTML.png

2. In the list that appears, click **Text**.

   An empty component appears at the bottom of the Unit.
   
  .. image:: Images/HTMLComponent_Edit.png
   
3. In the empty component, click **Edit**.
   
   The HTML Component Editor opens. 
  
  .. image:: Images/HTMLEditor.png

4. Click **Settings** to enter the **Display Name** for the HTML component. 

   A student sees the Display when hovering your mouse over the icon for the Unit in the Subsection accordian. 

   Click **Save** to return to the Component Editor. 

5. Enter text as needed. 

6. Click **Save** to save the HTML component.

For more information, see:

* :ref:`Work with the Visual and HTML Editors`
* :ref:`Add a Link in an HTML Component`
* :ref:`Add an Image to an HTML Component`






.. _Add a Link in an HTML Component:

***********************************
Add a Link in an HTML Component
***********************************

.. _Add a Link to a Website:

============================
Add a Link to a Website
============================

.. _Add a Link to a File:

============================
Add a Link to a File
============================

You can add a link in an HTML component to any file you uploaded for the course. 

Find any copy the URL of the file in the Files & Uploads page.

See :ref:`Add Files to a Course` for more information.

While editing the HTML component:

#. Switch to the HTML view.

#. To create a link to a document, enter the following syntax, where URL OF FILE is the URL that you copied from the Files & Uploads Page and LINK TEXT is the text that the user will click. 
   
   ``<p><a href="[URL OF FILE]">[LINK TEXT]</a></p>``


.. _Add a Link to a Course Unit:

============================
Add a Link to a Course Unit
============================

You can add a link to a course unit in an HTML component.

#. Determine the unit identifier of the unit you're linking to. To do this, open the
   unit page in Studio, and locate the **Unit Identifier** field under **Unit Location** in the right pane.

#. Copy the unit identifier.

#. Open the HTML component where you want to add the link.

#. Select the text that you want to make into the link.

#. Click the link icon in the toolbar.

#. In the Insert/Edit Link dialog box, enter the following in the Link URL field.
   
   Make sure to replace <unit identifier>(including the brackets) with the unit
   identifier that you copied in step 2, and make sure to include both forward slashes (/).
   
   ``/jump_to_id/<unit identifier>``

#. If you want the link to open in a new window, click the drop-down arrow next to
   the Target field, and then select Open Link in a New Window. If not, you can leave the default value.
   
#. Click **Insert**.

#. Save the HTML component and test the link.


.. _Add an Image to an HTML Component:

***********************************
Add an Image to an HTML Component
***********************************

You can add an any image that you have uploaded for the course to an HTML component. 

Find any copy the URL of the image in the Files & Uploads page.

See :ref:`Add Files to a Course` for more information.

.. note::  Review :ref:`Best Practices for Describing Images` when adding images to HTML components.

While editing the HTML component:

#. Switch to the HTML view.

#. To add the image to a document, enter the following syntax, where URL OF FILE is the URL that you copied from the Files & Uploads Page. 
   
   ``<p><img src="[URL OF FILE]"/></p>``


.. _HTML Templates:

**************
HTML Templates
**************

There are four kinds of HTML templates.

.. _Text Template:

=============================
Text Template
=============================

Most common - will use most frequently

NO PLACEHOLDER TEXT

.. _Announcement Template:

=============================
Announcement Template
=============================

When you create a new HTML component, you can select to use a built-in Announcement template.

When creating the new HTML component, select **Announcement**.

.. image:: Images/HTML_Component_Type.png
 :width: 600
 
The following screen opens.

.. image:: Images/image073.png

Edit the content of the announcement just as you would any HTML component.


.. _Use the Anonymous User ID Template:

============================
Anonymous User ID Template
============================

When you create a new HTML component, you can select to use a built-in Anonymous User ID template.

The Anonymous User ID template contains HTML set up for you to use a Qualtrics survey in your course.

When creating the new HTML component, select **Anonymous User ID**.

.. image:: Images/HTML_Component_Type.png
 :width: 600

Edit the content just as you would any HTML component.

To use your survey, you must edit the link in the template to include your university and survey ID.  

You can also embed the survey in an iframe in the HTML component.

For more details, read the instructions in the HTML view of the component. 


.. _Zooming Image Template:

============================
Zooming Image Template
============================

:ref: `Zooming Image`