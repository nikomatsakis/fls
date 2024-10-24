```{default-domain} spec
```

# Macros By Example

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