import re  # Add this import

class OCRVotingSystem:
    """Voting system to combine multiple OCR results"""
    
    @staticmethod
    def extract_features(text):
        """Extract features from text for comparison"""
        features = {
            'length': len(text),
            'lines': len(text.split('\n')),
            'has_if': 'if' in text.lower(),
            'has_else': 'else' in text.lower(),
            'has_for': 'for' in text.lower(),
            'has_print': 'print' in text.lower(),
            'has_equals': '=' in text,
            'has_percent': '%' in text,
            'has_parentheses': '(' in text and ')' in text,
            'has_colon': ':' in text,
            'numbers': len(re.findall(r'\d+', text)),
        }
        return features
    
    @staticmethod
    def calculate_similarity(text1, text2):
        """Calculate similarity between two texts"""
        if not text1 or not text2:
            return 0
        
        # Simple word overlap
        words1 = set(text1.lower().split())
        words2 = set(text2.lower().split())
        
        if not words1 or not words2:
            return 0
        
        intersection = words1.intersection(words2)
        union = words1.union(words2)
        
        return len(intersection) / len(union) if union else 0
    
    @staticmethod
    def vote(results):
        """Vote on multiple OCR results"""
        if not results:
            return None
        
        # Group similar results
        groups = []
        used = set()
        
        for i, (text1, score1) in enumerate(results):
            if i in used:
                continue
            
            group = [(text1, score1)]
            used.add(i)
            
            for j, (text2, score2) in enumerate(results):
                if j in used:
                    continue
                
                similarity = OCRVotingSystem.calculate_similarity(text1, text2)
                if similarity > 0.7:  # Similar threshold
                    group.append((text2, score2))
                    used.add(j)
            
            groups.append(group)
        
        # Pick the best group
        if not groups:
            return results[0][0] if results else None
        
        best_group = max(groups, key=lambda g: sum(s for _, s in g) / len(g))
        
        # Return the longest text in the best group
        return max(best_group, key=lambda x: len(x[0]))[0]