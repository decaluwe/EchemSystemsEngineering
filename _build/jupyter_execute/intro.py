#!/usr/bin/env python
# coding: utf-8

# # **_Modeling Electrochemical Systems:_ Introduction**
# 
# Steven C. DeCaluwe, Colorado School of Mines
# 
# ## Goals and Scope
# 
# Welcome! The purpose of this book is to give a general overview of electrochemical systems and how to model them. In this book, we will cover:
# - **Basics of electrochemistry**: electrochemical thermodynamics, kinetics, and transport,
# - **Features of electrochemical systems**: electrodes, electrolytes, and balance-of-plant,
# - **Electrochemical system operation**: use cases, operating modes,  how to evaluate performance, and
# - **Electrochemical Modeling**: Building and using software tools to model electrochemical systems.
# 
# ## What is Electrochemistry, and Why do We Care?
# 
# Electrochemistry can be thought of as a subset of chemistry, where chemical reactions are accompanied by the movement of charge between reactants and products. If the charge moves from one phase to another phase, the total electric potential energy of the system changes, during the course of the reaction. This has three practical implications of interest to us:
# 1. The potential energy of the various phases involved will influence the reaction rate, and can be varied to drive the reaction in one direction or another, 
# 2. The movement of charge results in an electrical current, which can be measured and therefore provides a measure of the reaction rate, and
# 2. The reaction can be used to either store or release electrical energy.
# 
# These three aspects of electrochemical reactions have led to the ubiquitous use of electrochemistry and electrochemical systems throughout society, for energy storage, conversion, and production, chemical processing, and sensors, among others. In recent years, advances in electrochemical systems (such as batteries) have led to a revolution in portable power for consumer devices and a rapid proliferation of electric mobility options (e.g. [Fig. 1](battery-charge-fig) and [2](PEV-sales)). Moreover, the ability to couple efficient electrochemical storage solutions with intermittent renewable power sources (e.g. solar and wind) will support attempts to decarbonize our energy infrastructure and mitigate human impacts on Earth's climate and biodiversity. Beyond energy storage and conversion, electrochemical systems play an important role in a range of industrial chemical applications, as discussed in [Chapter 2](chapters/ch2-devices-and-systems/ch2-content.md). 
# 
# ```{figure} images/EV.png
# :name: battery-charge-fig
# :width: 75%
# 
# Advances in electrochemical devices and systems development have enabled portable power applications, such as plug-in electric vehicles. Photo by <a href="https://unsplash.com/@chuttersnap?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">CHUTTERSNAP</a> on <a href="https://unsplash.com/s/photos/electric-car?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
#   
# ```
# ## Improving Electrochemical Systems
# 
# Improved electrochemical devices and systems are associated with numerous benefits. These range from improved standards of living, abatement of anthropogenic climate effects and associated improvements in public health, and new classes of jobs and economic output, among others.  However, several challenges and risks associated with increasing use of electrochemical devices must also be addressed and/or managed. These include the extraction of and supply chain for critical minerals (and associated social justice issues associated with environmental degradation and labor conditions in mineral-rich regions), device safety and durability, and new electrical infrastructure requirements. To leverage opportunities while mitigating risks, it is necessary that we develop a thorough, quantitative understanding electrochemical device operation. If we can understand and predict device performance for a variety of device designs, operating conditions, and applications, we can both develop improved devices and design electrochemical systems that build on their strengths.
# :::{figure-md} PEV-sales
# <img width="512" alt="Comparison PEV sales China Europe USA from 2014" src="https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Comparison_PEV_sales_China_Europe_USA_from_2014.png/512px-Comparison_PEV_sales_China_Europe_USA_from_2014.png">
# 
# 
# Better, more durable electrochemical devices will be required to mitigate risks associated with extraction and supply chains for critical minerals required by increasing demand for these devices. <a href="https://commons.wikimedia.org/wiki/File:Comparison_PEV_sales_China_Europe_USA_from_2014.png">Mariordo (Mario Roberto Durán Ortiz)</a>, <a href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0</a>, via Wikimedia Commons.
# :::
# ## Numerical Modeling and Simulation
# 
# In this book, we use numerical simulations as a lens for understanding the performance of electrochemical systems. Performance is determined by a wide and interdiscplinary range of factors, including materials science, thermodynamics, chemical kinetics, fluid dynamics, and manufacturing. Numerical simulations provide us a framework in which we can describe these factors quantitatively, combining various phenomena so that we can predict the degree and ways in which each influences device and system performance.  
# 
# The book covers fundamental processes such as charge-transfer and chemical reactions, heat transfer, and species transport, describing equations to describe each process. These are incorporated into models via governing equations which describe the evolution of the device's _state_, given the processes modeled and the _boundary conditions_ assumed/implemented.
# 
# At present, this book presents models within a _one-dimensional_ _continuum_ framework.  To be sure, state of the art models typically include multi-scale simulations with both nanometer-scale and device-scale effects, and extend to two and three dimensions. However, we limit the scope here with the aim of improving clarity and providing a basic understanding of electrochemical principles. We feel that the interested reader can readily extend these intermediate-scale models to incorporate multi-scale phenomena and/or extend model dimensionality, while also providing model outputs that can be coupled with system-level analysis. The book is not meant to be exhaustive; we refer to the great wealth of other wonderful texts on these topics, for readers interested in a deeper dive. At the same time, it is also not necessarily meant to be read cover-to-cover. We aim to present depth on a range of topics relevant to electrochemical systems.  On any given topic, it is recommended that you read only to the level of detail that suits your current interests. Beyond the introductory material, the reader should be able to pick and choose individual chapters, as their interest, abilities, and needs dictate.
# 
# ## Beyond Model Development
# 
# As you will see, building numerical simulation tools is about much more than writing code. In addition to defining the model scope and deriving governing equations, it is helpful to understand how electrochemical systems are built, operated, and assessed.  In this text, we also therefore cover electrochemical system design and fabrication, electrochemical device operation and testing, and the characterization tools used to understand the evolution of the materials, interfaces, and structures involved in an electrochemical device during its lifetime.
# 
# ## Software and this Text 
# 
# The models in this text are all developed using readily available, open-source [Python](http://python.org)-based software tools.  We strive to give an introduction to some basic Python coding principles, tips and tricks, and approaches so that you can understand the code presented and build similar tools yourself.
# 
# This text is built using the [JupyterBook](http://jupyterbook.org) platform, which enables interactive code blocks intersperesed throughout the text.  For various examples, we will provide you with completed code blocks which you can execute/run _without having to leave this text_ and view the output.  For other cases, we will provide you with _incomplete_ code blocks, providing you and opportunity to write your own code in a supported manner, to gain practice and check your understanding. Wherever you see the {fa}`rocket` present at the top of a page, press {fa}`rocket`--> {guilabel}`Live Code` to enable interactive code blocks.
# 
# Try it out, below! After clicking {guilabel}`Live Code`, you will see three buttons appear:
# 
# ![buttons](images/CodeButtons.png)
# 
# Click on `run` to run the code block.  The first time you execute code, it will take some time to set up the links to the server where the code is actually run (up to a minute or more).  Do not be alarmed. All subequent code blocks will run much faster, after the initial set up.

# In[1]:


print("This is a string.")


# These are Jupyter code blocks.  Clicking on `run` will execute the Python code in that block. For those new to coding, feel free to edit the string with your own message, and re-run the code block to see the altered message printed out. Or add some calculations (try `x = 2**3`, for example) and then on a separate line print the variable's value (`print(x)`). Each time a Jupyter code block is executed, any variables created will be retained in the local memory and can be accessed in any code blocks subsequently run on that same page. Holding variables in local memory is one of the nice features of Jupyter. Once a block is successfully executed, you do not need to run it again.  For lengthy calculations or data imports, for example, this can be quite a blessing!
# 
# Note, however, that your calculations (or the person running them) can easily get "confused" if you run a code block multiple times or run them out of order. Say, for example, that you define three code blocks: Block 1 defines a variable called `var` (note: the following blocks are not interactive; they are just there to demonstrate).
# ```python
# var = 2
# ```
# Block 2 implements an intermediate step that doubles the value of `var` :
# ```python 
# var *= 2
# ```
# And block 3 takes the square root of `var`:
# ```python 
# result = var**(0.5)
# ```
# Clearly, the intended value of `result` is 2.  However, if the user, wittingly or otherwise, runs code block 2 twice in a row before executing code block 3, they would get `result = 2.828`.  If the user instead _skips_ the second code block, they would get `result = 1.414`. This is a relatively simple example, but demonstrates a common pitfall to Jupyter notebooks. See Joel Grus's [humorous talk](https://www.youtube.com/watch?v=7jiPeIFXb6U), for more thoughts on the topic.
# 
# 
# The other two buttons provide some degree of remedy from this problem. The `restart` button clears the local memory so that you can start fresh, while the `restart & run all` button clears out the local memory and runs all code blocks on that page, in the order that they appear. When in doubt, clearing the memory and running the updated blocks in the intended sequence is never a bad idea.
# 
# ## Suggesting Improvements
# Finally, this text exists as a repository on [GitHub](https://github.com).  Clicking the  {fab}`github` button at the top of the page will present an option to visit the code repository. The button also presents an `open issue` option, where one can submit any questions, concerns, or suggestions to help improve this book for future readers.
