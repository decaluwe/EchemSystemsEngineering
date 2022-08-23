# Chapter 1. Introduction to Electrochemistry

Electrochemistry is a branch of chemistry that deals with reactions that, in addition to transforming chemical bonds, transfer electrical charge between reactants and products.  Much of electrochemistry is concerned with changes that occur due to passage of electical current, and the resulting conversions between electrical and chemical energy. The field is commonly invoked with regard to energy storage and conversion, but electrochemical phenomena play significant roles in a broad array of applications, ranging from chemical production, chemical sensors, corrosion, and others {cite:labelpar}`bard_text_2022` See [Chapter 2](../../chapters/ch2-devices-and-systems/ch2-content.md) for a broader discussion of electrochemical systems and applications.

Electrochemistry is a rich and complex field whose theory and practice spans more than a century.  A complete and thorough description of electrochemical theory is beyond the scope of this chapter. Rather, we aim to give an overview of the primary features of what makes an electrochemical reaction.  In subsequent chapters we will introduce concepts and theory as needed to model electrochemical phenomena. In order to cover a breadth of systems and phenomena, this presentation, at the moment, does not reflect the depth and complexity of electrochemical theory. In order to enable the engineering of electrochemical systems, we leave a full accounting of electrochemical science to the wealth of other wonderful texts which exist on the topic, and encourage the reader to avail themselves of these resources.{cite:labelpar}`bard_text_2022, fuller_text_2018, newman_text_2021`

## Electrochemical Reactions
Electrochemical reactions, also called _charge transfer reactions_, take place at the interface between two materials (_phases_). As the name implies, the reaction is considered a charge transfer reaction (and hence an electrochemical reaction) if electrical charge is transferred from one phase to another.

For example, consider the simple cartoon in {numref}`charge-transfer-fig`. In the illustration on the left, a lithium cation (charge = +1) associates with anions (or, more accurately, withy negatively-charged portions of the polar solvent molecules) in the electrolyte to form a charge-neutral complex. Similarly, the electrode begins in a charge-neutral state. 

The charge-transfer reaction moves the Li$^+$ ion from the electrolyte into the electrode, transferring the positive charge to the electrode. The ion's chemical energy has changed, from the solvation complex in the electrolyte to a new configuration (for example, intercalated into graphite) in the electrode, with an associated change in chemical potential energy. Similarly, the electric potential energy of the electric charge may have changed, depending on the electric potential of the electrolyte and electrode.

```{figure} charge-transfer.png
:name: charge-transfer-fig
:width: 75%

Illustration of charge transfer at a phase boundary. On the left, a positively-charged lithium ion associates with a negatively-charged ion in the electrolyte to make a charge-neutral complex.  The electrochemical reaction moves the Li ion from the electrolyte to the electrode.  The reaction is influenced both by the chemical energy of the Li ion before and after the reaction and by the electric potential energy of the charge in each of the two phases.
```

The charge transfer can be written thusly:

$$ {\rm Li^+_{elyte} \leftrightharpoons Li^+_{ed}}$$

where the subscripts `elyte` and `ed` represent the phases where the species is located (the electrolyte and the electrode, respectively).  Because the anion/solvent complex does not change phases (it begins and ends in the electrolyte), it does not _explicitly_ need to be included in the reaction equation. However, it would not be _incorrect_ to include it, and certain authors may indeed have compelling reasons to do so. In particular, if one considers that the solvent molecules are no longer part of a solvation complex after the reaction, and therefore exist in different chemical states before and after the reaction, one may rightly consider them to be different species.  While we delve into these details in later chapters, we have opted for the simpler presentation, in this introduction.


The rate of the charge transfer reaction (in moles per second, for example), can be converted to an equivalent charge transfer current (in Amperes, or Coulombs per second).  The current internal to the cell which occurs due to a charge transfer reaction is often referred to as a _Faradaic current_ $i_{\rm Far}$, and the conversion between reaction rate and the Faradaic current is known as *Faraday's Law*:

$$ i_{Far} = \frac{\dot{q}_{\rm rxn}}{nF}.$$

Here $\dot{q}_{\rm rxn}$ is the rate of progress of the reaction (mol s$^{-1}$), $n$ is the number of elementary electrical charge units transferred to the electrode (moles of charge per mole of reaction), and $F$ is _Faraday's constant_, the number of Cuolombs contained in a mole of elementary charge units ($F$ = 96485 C mol$^{-1}_{\rm charge}$).

_Notes on nomenclature and sign convention_: 
- As you will no doubt find, sign conventions in electrochemistry are fairly arbitrary; there is no universal rule for what we mean, for instance, by "positive" current.  In this book, we will always take _positive current_ to mean _positive charge delivered to the electrode_.  Note that Faraday's Law is correct, regardless of this assumption.  If we switch our sign convention, the signs on $n$ and $i_{\rm Far}$ will both change, meaning that Faraday's Law still holds.
- The variable $n$ is sometimes referred to as the "number of electrons" transferred by the reaction (it is sometimes even written as $n_{\rm elec}$).  While this is perhaps more intuitive and easier to grasp (it is also more eloquent), we find that it is not sufficiently generalized.  In the reaction above, for example, no electrons are transferred, but electrical charge does indeed transfer from one phase to another. The phrase "number of electrons" is also inconsistent with our assumed sign convention, which concerns itself with the movement of positive charge.  For clarity, please note that "one unit of elementary charge" is equal and opposite to the charge of one electron.

After the charge transfer reaction, in the illustration on the right, the electrolyte and electrode are no longer charge neutral, indicating that positive charge has been transferred from the electrolyte to the electrode. A point emphasized throughout this text is that the bulk interior or phasese strongly prefers to remain _charge neutral_. The positive charges in the phase are "balances" by an equal number of negative charges. If the bulk of a phase departs from this charge neutral state, large electrostatic forces (in the form of an electric field) will quickly develop.

In this particlar case, there are two possible pathways to maintain charge neutrality:
- If there is a source of external current may deliver a electric charge in the form of electrons to compensate for the positive charge transferred to the electrode by the charge transfer reaction.
- If the charge  two charges would likely be strongly attracted to one another, forming a charged double layer at the electrode-electrolyte interface. If the double layer continues to build, an electric potential difference will grow at the phase interface, which will, in turn, impact the ability to transfer additional charge via charge transfer reactions.  These details are covered in detail in 

The ultimate impact of $i_{\rm Far}$ in a device depends on the boundary conditions - how the device is operated. These details--calculating Faradaic currents, double layer currents and potentials, and external currents--are discussed in greater detail in the coming chapters ([Chapter 4](../../chapters/ch4-charge-transfer/ch4-content.md)).

Regardless of the specific details, at steady state know that the external current will equal the Faradaic current internal to the cell.  Any transient double layer currents will be resolved fairly quickly (< 1 s), adjusting the electric potentials internal to the cell until $i_{\rm Far} = i_{\rm ext}$. For all practical purposes, then, the external current serves as a reliable measure of the Faradaic current and hence the reaction rate of the charge transfer reactions within the any electrochemical device. This has important pracitcal and technlogical implications, in that the external current can therefore be used to either _control_ the charge transfer reaction rate (to produce desired chemical products at a known rate), or to _measure_ the rection rate, which provides information about the chemicals present inside the device at any given time, such as in electrochemical sensors.  The thoery, equations, and rotines presented in this book will provide the reader with the tools to measure, design, and control devices for practical applications such as these.


## Electrodes and Electrolytes

## Electrochemical Devices


```{bibliography}
:style: plain
```