def classify_problem(transcription):
    keywords = {
        'cancellation': ['cancel', 'cancellation', 'canceled'],
        'reschedule': ['reschedule', 'change flight'],
        'refund': ['refund', 'compensation'],
        'delay': ['delay', 'delayed'],
        'staff_behavior': ['rude', 'unprofessional', 'behavior'],
        'miscellaneous': ['other', 'miscellaneous', 'issue']
    }
    
    for problem, keys in keywords.items():
        for key in keys:
            if key in transcription.lower():
                return problem
    
    return 'miscellaneous'  # Default if no specific problem identified
