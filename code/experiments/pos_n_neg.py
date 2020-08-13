# count if it is a positive word
        if word in p_list:
            if word in word_count_positive.keys():
                word_count_positive[word] += 1
            else:
                word_count_positive[word] = 1
  # else see if it is a negative word
        elif word in n_list:
            if word in word_count_negative.keys():
                word_count_negative[word] += 1
            else:
                word_count_negative[word] = 1
        else: # do nothing
            pass