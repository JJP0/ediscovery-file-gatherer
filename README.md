# ediscovery-file-gatherer
 Moves emails from an eDiscovery export to a flat folder structure rather than their original embedded folder structure.


# Use case

I have found this to be useful in the following scenarios
- Simplified management of an eDiscovery export, when the origin of the email isn't required
- Simplified reading of a large eDiscovery export (open, read, close, next email, etc.) due to all emails being listed next to eachother
- Some legal scenarios may require emails to be exported into a 3rd party tool for analysis, this assists with those exports.

# Note

For emails that share the same name as a result of multiple replies or forwards (RE:, FW:), they will be prefaced with a number to allow them to be stored in the same directory.
If you require the filename to exactly match the email subject, this won't work.
