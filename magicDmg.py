def take_magic_damage(health, resist, amp, spell_power):
    max_dmg = spell_power * amp
    damage_dealt = max_dmg - resist
    return health - damage_dealt
