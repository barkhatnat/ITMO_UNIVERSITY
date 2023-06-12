with open("input.txt", "r") as input_file:
    results = []
    for line in input_file.readlines():
        line = line.split()
        mismatch_tolerance = int(line[0])
        text = line[1]
        pattern = line[2]
        result = []
        text_index_max = len(text) - len(pattern) + 1
        print(text_index_max)
        for text_index in range(text_index_max):
            missed = 0
            for pattern_index in range(len(pattern)):
                text_char = text[text_index + pattern_index]
                pattern_char = pattern[pattern_index]
                if text_char != pattern_char:
                    missed += 1
                if missed > mismatch_tolerance:
                    break

            if missed == mismatch_tolerance:
                match = text[text_index: text_index + len(pattern)]
                result.append(text_index)
        if len(result) == 0:
            results.append([0])
        else:
            results.append([len(result)] + result)
        with open("output.txt", "w") as output_file:
            for result in results:
                output = ""
                for i in result:
                    output += str(i) + " "
                output_file.write(output + "\n")
