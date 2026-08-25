Software & Tools
================

Throughout my research, I have developed and contributed to several open-source software resources for the Adaptive Optics community. 

SPECULA
-------
**Python AO end-to-end simulator**

SPECULA is a Python-based, object-oriented software derived from PASSATA and developed by the Adaptive Optics group at the Arcetri Observatory for end-to-end Monte-Carlo simulations of adaptive optics systems. It can be accelerated using GPU-CUDA via CuPy.

* `GitHub Repository <https://github.com/ArcetriAdaptiveOptics/SPECULA>`_
* `Documentation <https://specula.readthedocs.io>`_
* `Reference Paper <https://doi.org/10.1117/1.JATIS.12.1.019001>`_ (Rossi, Puglisi & Agapito, 2026)

SynIM
-----
**Synthetic Interaction Matrix generator for Adaptive Optics systems**

SynIM is a Python package for computing synthetic interaction matrices, projection matrices, and covariance matrices for AO systems. It supports SCAO, LTAO, GLAO, and MCAO configurations with Shack-Hartmann sensors, featuring GPU acceleration via CuPy.

* `GitHub Repository <https://github.com/ArcetriAdaptiveOptics/SynIM>`_
* `Documentation <https://synim.readthedocs.io>`_
* `Reference Paper <https://doi.org/10.1117/12.3102711>`_ (Agapito, Rossi & Puglisi, 2026)

TIPTOP
------
**Fast AO PSF Prediction Algorithm**

TIPTOP is a fast algorithm producing the expected Adaptive Optics Point Spread Function (PSF) for existing AO observing modes (SCAO, LTAO, MCAO, GLAO) under any atmospheric conditions. Based on an analytical approach in the Fourier domain, it reaches very fast computation times (few seconds per PSF with GPU).

* `GitHub Repository <https://github.com/astro-tiptop/TIPTOP>`_
* `Documentation <https://astro-tiptop-services.github.io/astro-tiptop-services/>`_
* `Reference Paper <https://doi.org/10.1117/12.2561533>`_ (Neichel et al., 2021)

Semi-analytic-Error-Budget
--------------------------
**P-WFS Error Budget Simulator**

A semi-analytic simulator for the Pyramid Wavefront Sensor (P-WFS) Error Budget, based on the theoretical framework presented in Agapito et al. 2019.

* `GitHub Repository <https://github.com/ArcetriAdaptiveOptics/Semi-analytic-Error-Budget>`_
* `Reference Paper <https://doi.org/10.1117/1.JATIS.5.4.049001>`_ (Agapito & Pinna, 2019)

PASSATA
-------
**IDL AO end-to-end simulator**

PyrAmid Simulator Software for Adaptive opTics Arcetri (PASSATA) is an IDL-based object-oriented software developed in the Adaptive Optics group of the Arcetri Observatory for Monte-Carlo end-to-end adaptive optics simulations. 

* `GPU-CUDA Acceleration DLL <https://github.com/ArcetriAdaptiveOptics/IdlTools/tree/main/GPU>`_
* `Reference Paper <https://doi.org/10.1117/12.2233963>`_ (Agapito, Puglisi & Esposito, 2016)