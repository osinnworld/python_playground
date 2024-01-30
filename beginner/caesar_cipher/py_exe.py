#!/bin/bash

for file in *.py; do
    if [ -f "$file" ]; then
        # Check if the file already contains the shebang line
        if ! grep -q "#!/usr/bin/python3" "$file"; then
            # Add the shebang line only if it doesn't exist
            echo -e "#!/usr/bin/python3\n$(cat $file)" > "$file"
        fi
    fi
done

chmod +x *.py
