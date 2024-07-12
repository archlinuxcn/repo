Version 6.0
===========

Overview
--------
* The FuzzyLite Libraries, namely fuzzylite and jfuzzylite, both in version 6.0, are licensed under the GNU General Public License version 3.

* By default, fuzzylite builds using C++11 instead of C++98. 

* Important performance improvements.

* Refactored the following names for the operation of engines: from activation operator to implication operator, from accumulation operator to aggregation operator.

* Renamed the term `Accumulated` to `Aggregated`.

* New activation methods decouple the activation of rules from the rule block and provide different methods for activating rules (see Activation Methods).

* New class `ActivationFactory` provides a factory of activation methods.

* New class `Benchmark` to evaluate the performance and accuracy of engines.

* New class `Complexity` to estimate the computational complexity of an engine.

* New class `RScriptExporter` to export the surfaces of an engine using the `ggplot2` library.

* New class `Binary` term for binary edges.

* New `UnboundedSum` S-Norm in `SNormFactory`.

* New classes `SNormFunction` and `TNormFunction` to create custom functions on any two values using the `Function` class.

* Added description strings to `Engine`, `Variable` and `RuleBlock`

* Privatized previously protected members of classes and subclasses of `Term`, `Variable`, `Rule`, `Defuzzifier`, `[Cloning|Construction]Factory`, `Importer`, `Exporter`, amongst others.

* Improved portability by replacing `int` for `std::size_t` where necessary, thereby additionally removing warnings in Windows 64bit

* Deleted `Operation.cpp` and inlined its methods into `Operation.h`

* Updated `.travis.yml` to use Docker, and build using g++ (versions 6, 5, 4.9, 4.8, 4.7) and clang (versions 3.8, 3.7, 3.6, and 3.5). 

* Added `appveyor.yml` to use continuous integration in Windows under Visual Studio 2013 and 2015.

* Added some unit tests and support for future unit tests.

* Bug fixes.

* New example of hybrid engines.

* New example on obstacle avoidance for Mamdani, Takagi-Sugeno, and Hybrid engines.

* New R scripts for each example and its respective surfaces in `pdf` formats.


Activation Method
-----------------
* New activation methods determine the activation of rules in a rule block. Specifically, the activation methods compute the activation degrees of the rules and the activation order of the rules.

* Seven activation methods available: General, First, Last, Highest, Lowest, Proportional and Threshold.

* If no activation method is supplied, an instance of General will be automatically set.

* New class `General` activates every rule following the insertion order in the rule block.

* New classes `First` and `Last` activate the first and last $n$ rules (following insertion order) whose activation degrees are greater than or equal to a given threshold.

* New classes `Highest` and `Lowest` activate the first and last $n$ rules sorted (descending or ascending) by activation degree.

* New class `Proportional` activates every rule with an activation degree proportional to the activation degrees of the other rules.

* New class `Threshold` activates every rule that satisfies a given comparison operator and a given threshold.

* New class `ActivationFactory`  provides a factory of activation methods.



Defuzzifier
-----------
* Overall performance improvements
* The new default resolution of integral defuzzifiers is 100 (from 200 in previous version)
* Importantly simplified `WeightedAverage` and `WeightedSum` by not using the implication and aggregation operators.
* New experimental classes  `WeightedAverageCustom` and `WeightedSumCustom` which use the implication and aggregation operators to compute the weighted averages and weighted sums, respectively.


Factory
-------
* New class `ActivationFactory` to register activation methods.
* New method `FactoryManager::activation()` to get the activation factory.
* Inlined methods in [CloningFactory|ConstructionFactory].h
* Fixed bug in `CloningFactory::deregisterObject()`. Bug: Object was deleted before removing it from the map, leaving an invalid object in the map which would cause a segmentation fault. Solution: Remove the object from the map before deleting it.
* New `abs` function in `FunctionFactory` to compute the absolute value of a number.
* New `UnboundedSum` S-Norm in `SNormFactory`.

Hedge
-----
* Added `FL_IOVERRIDE` identifiers to hedge Extremely
* Added `FL_IFINAL` final identifiers to `Hedge` classes (except `Any`).



Importer and Exporter
---------------------
* New `RScriptExporter` generates an R script that uses the `ggplot2` library to produce the surfaces of an engine for each pair of input variables on each output variable.

* Updated `Fll[Importer|Exporter]` to import and export the newly named properties `implication` and `aggregation` (previously known as `activation` and `accumulation`). However, the `FllImporter` has backward compatibility with the previous property names.

* In `Fll[Importer|Exporter]`, added `lock-range` property of input variables,  `activation` property for activation methods in rule blocks, and `description` property to `[Input|Output]Variable` and `RuleBlock`.

* Added default option to generate C++ and Java code using the actual names of the input variables, output variables, and rule blocks, instead of the generic  `[input|output]Variable` and `ruleBlock` names.

* Updated [Cpp|Java][Import|Export] to generate code using the `description` of an engine if available, the `implication` instead of the `activation`, and the `aggregation` instead of the `accumulation`.

* Removed compatibility between `[Fcl|Fis]Exporter` and `fuzzylite`. In previous versions, these exporters produced additional tags that were only relevant to `fuzzylite`, so that an engine written in these languages could also support the features in `fuzzylite`. However, in doing so, Matlab, Octave and JFuzzyLogic would fail to import the engines written in their own languages because they would not recognize the `fuzzylite` features. Hence, in order to generate code compatible with Matlab, Octave, and JFuzzyLogic, the `fuzzylite` features are removed from the code. 

* Refactored methods [Cpp|Java|Fll|Fis|Fcl]Exporter::toString([S|T]Norm*) to take `::toString(Norm*)`.

* Renamed methods FisImporter::extract[SNorm|TNorm|Defuzzifier]() to FisImporter::translate[SNorm|TNorm|Defuzzifier]()

* Fixed bug causing segmentation fault when malformed term in FuzzyLite Language



Norms
-----
* New class `UnboundedSum` to compute sum between any two values and hence reflect Matlab's and Octave's `sum` aggregation operator.
* New classes `SNormFunction` and `TNormFunction` to create custom functions on any two values using the `Function` class.
* Fixed bug computing the `NormalizedSum` S-Norm.


Rule
----
* Added properties `fl::scalar activationDegree`, `bool triggered` and `bool enabled` to a `Rule`. The `activationDegree` property stores the activation degree of the rule in order to avoid recomputing it when requesting it. The `triggered` property indicates whether the rule was triggered (i.e., whether the antecedent modified the consequent). The `enabled` property determines whether the rule can be triggered (by default, a rule is always enabled unless programmatically indicated otherwise).

* Decoupled computing the activation degree and triggering the rule. Previously, the activation degree of a rule was computed and triggered at the same time using `Rule::activate(TNorm* conjunction, SNorm* disjunction, TNorm* implication)`. Currently, there are two methods: `fl::scalar activateWith(TNorm* conjunction, SNorm* disjunction)`, which computes, stores and returns the activation degree of the rule; and `trigger(TNorm* implication)`, which, if the rule is enabled and the activation degree is greater than zero, then the rule is triggered to modify the consequent.

* Renamed `RuleBlock::activation` operator to `RuleBlock::implication` operator, and so its respective getters and setters.
* Added `RuleBlock::activation` method and respective getters and setters.
* In `RuleBlock::activate()`, if there is no activation method, the `General` activation method is automatically set in order to have backward compatibility.

* Fixed bug in `RuleBlock` to reset and clone the implication operator. Bug: implication operator is not copied and reset. Fix: copy and reset implication operator when cloning the `RuleBlock`.

* Added identifier `FL_IFINAL` to classes `Proposition` and `Operator`.

Term
----
* Performance improvements.
* `Discrete` term uses binary search instead of linear search, hence significantly improving performance.
* `Discrete` term can create a `Discrete` term from any other term.
* New `Binary` edge term.
* Added method `bool Term::isMonotonic()` to determine whether the term is monotonic (returns true only for `Concave`, `Ramp`, `Sigmoid`, `SShape`, and `ZShape`).
* Refactored static method `WeightedDefuzzifier::tsukamoto()` into non-static method `Term::tsukamoto()`, which is overriden by each of the terms that can be used for `tsukamoto` controllers.
* Privatized `Term::name` and the properties of each subclass of `Term`.
* Inlined generic methods in `[Linear|Discrete].h`
* Renamed `Activated::activation` operator to `Activated::implication` and its respective getters and setters.
* Renamed `Accumulated` term to `Aggregated` term, and its `accumulation` operator to `aggregation` operator including getters and setters.
* For performance improvements, terms of `Aggregated` term are copies of objects in stack memory rather than pointers to objects in heap memory.
* Refactored static `Term::updateReference()` to non-static being overrided by `Linear`, `Function`.
* Added enum `[Ramp|Sigmoid]::Direction` to specify the direction of the term.
* Added `Term::clone()` method to create a copy of any term.

* Fixed bug in `Function` term. Bug: given a formula = "tan(y)" and a map["y"] = 1.0, and executing `Function::load(formula)`, then the map of variables is reset because `load()` calls `unload()` first, causing the deregistration of variable `y`. Solution: Removed method `unload()` from `load()`, thereby causing future `load()` not to reset variables.
* Fixed bug in `Function` when enclosing variable in double parenthesis.



Variable
--------
* Refactored `[Input|Output]Variable::[get|set][Input|Output]Value()` to a single value in `Variable::[get|set]Value()`.
* Refactored `OutputVariable::[is|set]LockedOutputValueInRange()` to its parent `Variable::[is|set]LockValueInRange()`.
* Added option to lock value in range to input variables by refactoring `OutputVariable::lockValueInRange` to `Variable::lockValueInRange`.
* Renamed `OutputVariable::[is|set]LockedPreviousValue()` to `OutputVariable::[is|set]LockPreviousValue()`.
* Added wrapping method `OutputVariable::[get|set]Aggregation()`.
* For performance improvements, added enum `Variable::Type` and methods `Variable::type()` to indicate whether the variable is of `Type::InputVariable` or `Type::OutputVariable`. Thus, it is no longer necessary to `dynamic_cast` variables to find out whether they are input or output variables.



Benchmark
---------
* Benchmark the time it takes your engine to perform a given number of evaluations (available only when building using C++11) over a given number of independent runs.
* Measure the accuracy of the engine using the mean squared error between the obtained values and the expected values.
* Export the benchmark results to text.

Complexity
----------
* New complexity methods in the components involved in the operation of an engine.
* Complexity methods are completely decoupled from the operation of an engine, so they do not affect the performance of the engines.

Console
-------
* Benchmark engines from the FuzzyLite Console
* Hybrid example in Console

Engine
------
* Description string for Engine
* Changed signature of `::configure(TNorm* conjunction, SNorm* disjunction, TNorm* activation, SNorm* accumulation, int resolution)` to `::configure(TNorm* conjunction, SNorm*  SNorm* disjunction, TNorm* implication, SNorm* aggregation, Activation* activation)`, where `implication` and `aggregation` are better names for activation and accumulation (respectively), and the `activation` refers to an activation method (see Activation Methods)

Exception.h
-----------
* Definition FL_BACKTRACE_OFF in Exception.cpp renamed to FL_BACKTRACE, hence functionality is changed. 

fuzzylite.h
-----------
* Removed definitions FL_VERSION, FL_DATE from fuzzylite.h
* Renamed fuzzylite::debug() to fuzzylite::isDebugging()
* Renamed fuzzylite::logging() to fuzzylite::isLogging()
* Inlined methods of fuzzylite.h
* Removed definition `FL_CPP11` and replaced it for `FL_CPP98`. By default, `FL_CPP98` is not defined, hence building using `C++11`.


Examples
--------
* New example of hybrid engines.
* New example on obstacle avoidance for Mamdani, Takagi-Sugeno, and Hybrid engines.
* New R scripts for each example and its respective surfaces in `pdf` formats.
* Updated examples to use the new properties  `InputVariable::lock-range`, `Engine::description`, `[Input|Output]Variable::description`, `RuleBlock::description`, `RuleBlock::implication`, `RuleBlock::activation`, and `OutputVariable::aggregation`.
* Updated C++ and Java examples to reflect variable names instead of generic names.



