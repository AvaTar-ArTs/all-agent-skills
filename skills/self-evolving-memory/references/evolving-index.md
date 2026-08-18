# Evolving Index Patterns

## Memory Structure Evolution Rules

1. **Access Pattern Learning**: Frequently accessed entries get promoted
2. **Decay Mechanism**: Unused entries after 90 days get flagged for review
3. **Consolidation**: Similar entries merge automatically
4. **Relationship Discovery**: Co-accessed entries create links

## SQL Views for Memory Analysis

```sql
-- Recently active decisions
CREATE VIEW recent_decisions AS
SELECT * FROM decisions 
WHERE timestamp > datetime('now', '-30 days')
ORDER BY timestamp DESC;

-- High-frequency patterns
CREATE VIEW strong_patterns AS
SELECT * FROM patterns
WHERE frequency > 5 AND confidence > 0.7;
```
