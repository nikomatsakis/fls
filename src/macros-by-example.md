# Macros By Example

```{default-domain} spec
```

```{syntax}
MacroRulesDeclaration ::=
    $$macro_rules$$ $$!$$ Name MacroRulesDefinition

MacroRulesDefinition ::=
    $$($$ MacroRuleList $$)$$ $$;$$
    | $$[$$ MacroRuleList $$]$$ $$;$$
    | $${$$ MacroRuleList $$}$$

MacroRuleList ::=
    MacroRule ($$;$$ MacroRule)* $$;$$?

MacroRule ::=
    MacroMatcher $$=>$$ MacroTranscriber

MacroMatcher ::=
    $$($$ MacroMatch* $$)$$
    | $$[$$ MacroMatch* $$]$$
    | $${$$ MacroMatch* $$}$$

MacroTranscriber ::=
    DelimitedTokenTree

MacroMatch ::=
    MacroMatcher
    | MacroMatchToken
    | MacroMetavariableMatch
    | MacroRepetitionMatch
```

`macro_rules` allows users to define syntax extension in a declarative way.  We
call such extensions "macros by example" or simply "macros".

Each macro by example has a name, and one or more _rules_. Each rule has two
parts: a _matcher_, describing the syntax that it matches, and a _transcriber_,
describing the syntax that will replace a successfully matched invocation. Both
the matcher and the transcriber must be surrounded by delimiters. Macros can
expand to expressions, statements, items (including traits, impls, and foreign
items), types, or patterns.
