class Endereco:

    def __init__(self, string_address: str, printme=True):
        self.string_adress_output = None

        __possible_numbers_in_address = [
            str(n) in string_address.upper() for n in list(range(0, 10))+['S/N']]

        address_has_number = any(__possible_numbers_in_address)

        if not address_has_number:
            _hint = "\nPreencha S/N  não tenha número.\n"
            raise ValueError(
                f"ENTRADA INVÁLIDA! \033[1;31mNÚMERO DO ENDEREÇO\033[m não foi detectado.{_hint}Por gentileza, tente novamente!")

        # Palavra 'caso' omitida (referenciando aos objetos criados em main.py)
        # ex: caso1_a = 1_a; etc...

        if len(string_address.split()) == 2:
            # 1_a, 1_b, 1_c, 1___
            split_logic = "," if "," in string_address else None
            self.string_adress_output = tuple(
                string_address.split(split_logic))
        else:
            if "," not in string_address:
                _slice = 0
                for e, sa in enumerate(string_address):
                    if sa.isnumeric():
                        _slice = e

                        # 2_a, 2_b
                        if string_address[-1].isnumeric() or string_address[-3].isnumeric():
                            _slice -= 1
                            break
                # 3_a, 3_b
                _slice_calc = _slice + 1
                self.string_adress_output = (string_address[:_slice_calc].strip(),
                                             string_address[_slice_calc:].strip())

                # 3_d
                indexof_kword_no = string_address.find('No')
                if indexof_kword_no != -1:
                    self.string_adress_output = (
                        string_address[:indexof_kword_no].strip(), string_address[indexof_kword_no:].strip())
            # 3_c
            else:
                self.string_adress_output = string_address.split(',')
                self.string_adress_output = tuple([
                    v.strip() for v in string_address.split(',')])

            # 3_a, 3_b (sort 'output' attribute)
            if self.string_adress_output[0].isnumeric():
                self.string_adress_output = tuple(
                    self.string_adress_output[i] for i in range(len(self.string_adress_output)-1, -1, -1))

        if printme:
            print(self.string_adress_output)
