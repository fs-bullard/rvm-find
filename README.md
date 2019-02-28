
# Project: rvm-find
-----

Using the relevance vector machine (RVM) for data-driven discovery of PDEs, as in "Robust data-driven discovery of governing physical laws with error bars", Zhang and Lin (2018).

Code forked and adapted from JamesRitchie/scikit-rvm.

Given some spatio-temporal dataset, can we find the governing PDE from a library of candidate terms?

From the library of candidate terms- referred to as basis functions in the RVM code -the RVM constructs a sparse regression using type-2 maximum likelihood on the hyperpriors on each regression weight.


### Theory

The RVM is a sparse Bayesian analogue to the Support Vector Machine, with a
number of advantages:

* It provides probabilistic estimates, as opposed to the SVM's point estimates.
* Typically provides a sparser solution than the SVM, which tends to have the
  number of support vectors grow linearly with the size of the training set.
* Does not need a complexity parameter to be selected in order to avoid
  overfitting.

However it is more expensive to train than the SVM, although prediction is
faster and no cross-validation runs are required.

The RVM's original creator Mike Tipping provides a selection of papers offering
detailed insight into the formulation of the RVM (and sparse Bayesian learning
in general) on a `dedicated page`_, along with a Matlab implementation.

Most of this implementation was written working from Section 7.2 of Christopher
M. Bishops's `Pattern Recognition and Machine Learning`.




