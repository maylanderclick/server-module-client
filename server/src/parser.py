import json

class Parser:
  def __init__(self, parent):
    self.parent = parent

  def CSV_to_JSON(self, CSV):
    blocks = CSV.replace('\r', '').split('\n\n')
    
    def convertBlock(block):
      lines = block.split('\n')
      titles = lines[0].split(';')
      values = lines[1:-2]

      def convertLine(line):
        elems = line.split(';')
        result = dict()
        for i in range(len(titles)):
          key = f'{titles[i]}' or f'FIELD_{i}'
          value = elems[i] or ' '
          result[key] = value
        return result

      return list(map(convertLine, values))

    return list(map(convertBlock, blocks))